from sqlalchemy.orm import Session

from app.cache.redis_cache import RedisCache
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationRequest


class CalculatorService:

    def __init__(self,db: Session):
        self.db = db

    def calculate(self,request: CalculationRequest):

        operation = request.operation.lower()

        cache_key = (
            f"{operation}:"
            f"{request.num1}:"
            f"{request.num2}"
        )

        cached_result = RedisCache.get(cache_key)

        if cached_result:

            return Calculation(
                id=0,
                operation=operation,
                num1=request.num1,
                num2=request.num2,
                result=cached_result["result"]
            )

        if operation == "add":
            result = request.num1 + request.num2

        elif operation == "subtract":
            result = request.num1 - request.num2

        elif operation == "multiply":
            result = request.num1 * request.num2

        elif operation == "divide":

            if request.num2 == 0:
                raise ValueError(
                    "Division by zero is not allowed"
                )

            result = request.num1 / request.num2

        else:
            raise ValueError(
                "Invalid operation"
            )

        calculation = Calculation(
            operation=operation,
            num1=request.num1,
            num2=request.num2,
            result=result
        )

        self.db.add(calculation)
        self.db.commit()
        self.db.refresh(calculation)

        RedisCache.set(
            cache_key,{
                "result": result
            }
        )

        return calculation

    def get_all_calculations(self):

        return (
            self.db.query(Calculation)
            .order_by(Calculation.id.desc())
            .all()
        )