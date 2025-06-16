from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):
    name: str
    age: int
    email: str
    course: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)