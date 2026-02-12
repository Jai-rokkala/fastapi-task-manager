from sqlalchemy.orm import Session
from models.user import User
from core.security import hash_password

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