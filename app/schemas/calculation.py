from pydantic import BaseModel

class CalculationCreate(BaseModel):
    expression: str
    result: float

class CalculationRead(BaseModel):
    id: int
    expression: str
    result: float
    class Config:
        orm_mode = True
