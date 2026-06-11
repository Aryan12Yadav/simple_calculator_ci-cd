from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.database.database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer,primary_key=True,index = True)

    operation = Column(String,nullable = False)

    num1 = Column(Float,nullable = False)

    num2 = Column(Float,nullable = True)

    result = Column(Float,nullable = False)
    



