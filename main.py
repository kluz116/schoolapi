from fastapi import FastAPI,status
from schemas import Student
from models import StudentModel
from database import engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.kluz.com",
    "https://localhost.kluz.com",
    "http://localhost",
    "http://localhost:3000",
     "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/root")
def getRoot():
    return{"Hello": "This is a school api"}

@app.post("/student", status_code=status.HTTP_201_CREATED)
def createStudent(student:Student):

    session = Session(bind=engine, expire_on_commit=False)

    students = StudentModel(first_name=student.first_name,last_name=student.last_name,age=student.age)
    session.add(students)
    session.commit()
    session.refresh(students)

    return "Student Created successfuly"

@app.get("/student/{id}")
def getStudent(id:int):
    session = Session(bind=engine, expire_on_commit=False)
    return session.query(StudentModel).filter(StudentModel.id == id).first()
    

@app.get("/student")
def getAllStudents():
    session = Session(bind=engine, expire_on_commit=False)
    return session.query(StudentModel).all()

@app.put("/students/{id}")
def updateStudents(student:Student,id:int):
    session = Session(bind=engine, expire_on_commit=False)
    obj = session.query(StudentModel).get(id)

    if obj:
        obj.first_name = student.first_name
        obj.last_name = student.last_name
        obj.age = student.age
        session.commit()
        session.close()

    return "Successfuly updated row.."

@app.delete("/students/{id}")
def deleteStudents(id:int):
    session = Session(bind=engine, expire_on_commit=False)
    obj = session.query(StudentModel).get(id)

    if obj:
        session.delete(obj)
        session.commit()
        session.close()


