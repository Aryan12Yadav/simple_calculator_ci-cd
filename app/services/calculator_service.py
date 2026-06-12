from sqlalchemy.orm import Session
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationRequest

class CalculationService:

    def __init__(self,db:Session):
        self.db = db

    def calculate(self,request:CalculationRequest):
        operation = request.operation.lower()

        if operation == "add":
            result = request.num1 + request.num2

        elif operation == "subtract":
            result = request.num1 - request.num2

        elif operation == "multiply":
            result = request.num1*request.num2

        elif operation == "divide":

            if request.num2 ==0:
                raise ValueError("Division by zero is not allowed")

        else:
            raise ValueError("Invalid operation")

        calculation = Calculation(operation = operation,
                                  num1 = request.num1,
                                  num2 = request.num2,
                                  result = result)

        self.db.add(calculation)
        self.db.commit()
        self.db.refresh(calculation)

        return calculation

    def get_all_calculations(self):
        return (self.db.query(Calculation).order_by(Calculation.id.desc()).all())
