
import uuid

from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

from pydantic import BaseModel

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.orm import Session

from database import Base
from database import engine
from database import get_db

app = FastAPI(
    title = "CalculatorAPI"
)

class Calculator(Base):
    __tablename__ = 'calculations'

    id = Column(Integer,Primary_key = True,index = True)

    user_id = Column(String,nullable = False)

    num1 = Column(Float,nullable = False)

    num2 = Column(Float,nullable = False)

    operation = Column(String,nullable = False)

    result = Column(Float,nullable = False)

    created_at = Column(DateTime,default = datetime.utcnow)

Base.metadata.create_all(bind = engine)

class CalculationRequest(BaseModel):
    num1:float
    num2:float
    operation:str


class Calculator:
    def add(self,num1,num2):
        return num1 + num2
    
    def subtract(self,num1,num2):
        return num1 - num2
    
    def multiply(self,num1,num2):
        return num1*num2
    
    def divide(self,num1,num2):
        if num2 == 0:
            raise HTTPException(
                status_code=400,
                detail = "Division by zero not allowed"
            )
        
        return num1/num2
    
    def calculate(self,num1,num2,operation):
        if operation == "+":
            return self.add(num1,num2)
        
        if operation == "-":
            return self.subtract(num1,num2)
        
        if operation == "*":
            return self.multiply(num1,num2)
        if operation == "/":
            return self.divide(num1,num2)
        
        raise HTTPException(status_code=400,detail = "Invalid operation")

calculator = Calculator()

def 