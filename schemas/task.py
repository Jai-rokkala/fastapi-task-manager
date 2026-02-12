from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

    class Config:
        from_attributes = True