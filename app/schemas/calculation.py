from pydantic import BaseModel
from pydantic import Field

class CalculationRequest(BaseModel):

    num1:float = Field(...,description="First number")

    num2:float = Field(...,description = "Second number")

    operation:str = Field(...,description="Operation name")

class CalculationResponse(BaseModel):
    id:int
    operation:str
    num1:float
    num2:float
    result:float

    class Config:
        from_attributes = True
        
