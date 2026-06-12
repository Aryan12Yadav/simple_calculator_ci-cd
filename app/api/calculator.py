from fastapi import APIRouter,Form
from fastapi import Depends
from fastapi import HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.calculation  import CalculationRequest,CalculationResponse
from app.services.calculator_service import CalculatorService


router = APIRouter(
    prefix = "/calculator",
    tags = ["Calculator"]
    )

@router.post("/calculate")
def calculate(
    num1: float = Form(...),
    num2: float = Form(...),
    operation: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        service = CalculatorService(db)

        request = CalculationRequest(
            num1=num1,
            num2=num2,
            operation=operation
        )

        return service.calculate(request)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
    

@router.get("/history",response_model=List[CalculationResponse])
def get_history(db:Session = Depends(get_db)):
    service = CalculatorService(db)

    return  service.get_all_calculations()