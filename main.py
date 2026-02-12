import email
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from db.database import SessionLocal, engine, Base
import schemas, core.security
from fastapi.middleware.cors import CORSMiddleware
from services import task_services, user_services
from models import task, user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    payload = core.security.decode_token(token)

    print("RAW TOKEN:", token)
    print("PAYLOAD:", payload)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Token missing subject")

    user = user_services.get_user_by_email(db, email)
    print("DB USER:", user)

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = user_services.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    return user_services.create_user(db, user.email, user.password)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not core.security.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = core.security.create_access_token({
        "sub": str(db_user.email),
        "role": db_user.role
        })
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=schemas.UserOut)
def read_me(current_user=Depends(get_current_user)):
    return current_user



@app.post("/api/v1/tasks", response_model=schemas.TaskOut)
def create_task_api(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return task_services.create_task(db, task.title, task.description, current_user.id)

@app.get("/api/v1/tasks", response_model=list[schemas.TaskOut])
def get_tasks_api(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return task_services.get_tasks(db)

@app.put("/api/v1/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task_api(
    task_id: int,
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    db_task = task_services.get_task(db, task_id)

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if db_task.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your task")

    return task_services.update_task(db, task_id, task.title, task.description)

@app.delete("/api/v1/tasks/{task_id}")
def delete_task_api(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    db_task = task_services.get_task(db, task_id)

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")

    task_services.delete_task(db, task_id)
    return {"message": "Task deleted"}



