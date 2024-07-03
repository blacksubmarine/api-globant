from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal, HiredEmployees, Departments, Jobs
import json

app = FastAPI()

# Pydantic models for request body
class HiredEmployeeCreate(BaseModel):
    id: int = None
    name: str
    hire_datetime: str
    department_id: int
    job_id: int

class DepartmentCreate(BaseModel):
    id: int = None
    department: str

class JobCreate(BaseModel):
    id: int = None
    job: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def log_invalid_records(table_name: str, records: list):
    with open(f"invalid_records_{table_name}.log", "a") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

def insert_records(db: Session, records: List[BaseModel], table_class):
    invalid_records = []
    for record in records:
        if record.id is None:
            invalid_records.append(record.dict())
        else:
            db_record = table_class(**record.dict())
            db.add(db_record)
    db.commit()
    if invalid_records:
        log_invalid_records(table_class.__tablename__, invalid_records)
    return {"status": "success", "invalid_records_count": len(invalid_records)}

@app.post("/hired_employees/")
def create_hired_employees(items: List[HiredEmployeeCreate], db: Session = Depends(get_db)):
    return insert_records(db, items, HiredEmployees)

@app.post("/departments/")
def create_departments(items: List[DepartmentCreate], db: Session = Depends(get_db)):
    return insert_records(db, items, Departments)

@app.post("/jobs/")
def create_jobs(items: List[JobCreate], db: Session = Depends(get_db)):
    return insert_records(db, items, Jobs)
