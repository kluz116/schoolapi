from pydantic import BaseModel,Field

class Student(BaseModel):
    first_name:str = Field(min_length=3,max_length=10)
    last_name:str = Field(min_length=3,max_length=10)
    age : int
    