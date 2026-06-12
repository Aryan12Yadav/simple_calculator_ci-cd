from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.calculation  import CalculationRequest,CalculationResponse
from app.services.calculator_service import CalculatorService


router = APIRouter(
    prefix = "/calculator",
    tags = ["Calculator"]
    )

@router.post("/calculate",response_model = CalculationResponse)
def calculate(request = CalculationRequest,
              db:Session = Depends(get_db)):
    try:
        service  = CalculatorService(db)
        return service.calculate(request)
    
    except ValueError  as error:
        raise HTTPException(
            status_code=400,
            detail =  str(error)
        )
    
@router.get("/history",response_model=list(CalculationResponse))
def get_history(db:Session = Depends(get_db)):
    service = CalculatorService(db)

    return  service.get_all_calculations()