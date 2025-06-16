from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students", response_model=schemas.Student)
def create(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/students", response_model=list[schemas.Student], include_in_schema=False)
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=schemas.Student)
def update(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated = crud.update_student(db, student_id, student)
    if updated is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@app.delete("/students/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db, student_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Deleted successfully"}
