from models.task import Task
from sqlalchemy.orm import Session

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