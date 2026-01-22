from sqlalchemy.orm import Session
from models import User
from auth import hash_password

def create_user(db: Session, email: str, password: str):
    hashed = hash_password(password)

    # If no users exist → make first user admin
    role = "admin" if db.query(User).count() == 0 else "user"

    user = User(email=email, hashed_password=hashed, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()



from models import Task

def create_task(db: Session, title: str, description: str, owner_id: int):
    task = Task(title=title, description=description, owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, title: str, description: str):
    task = get_task(db, task_id)
    if task:
        task.title = title
        task.description = description
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task
