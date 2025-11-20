from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/calculations", tags=["calculations"])

@router.post("", response_model=schemas.CalculationRead, status_code=status.HTTP_200_OK)
def create_calculation(calc: schemas.CalculationCreate, db: Session = Depends(get_db)):
    created = crud.create_calculation(db, calc)
    return created

@router.get("", response_model=list[schemas.CalculationRead])
def list_calcs(db: Session = Depends(get_db)):
    return crud.list_calculations(db)

@router.get("/{calc_id}", response_model=schemas.CalculationRead)
def read_calc(calc_id: int, db: Session = Depends(get_db)):
    calc = crud.get_calculation(db, calc_id)
    if not calc:
        raise HTTPException(status_code=404, detail="Not found")
    return calc

@router.put("/{calc_id}", response_model=schemas.CalculationRead)
def update_calc(calc_id: int, calc_in: schemas.CalculationCreate, db: Session = Depends(get_db)):
    updated = crud.update_calculation(db, calc_id, {"expression": calc_in.expression, "result": calc_in.result})
    if not updated:
        raise HTTPException(status_code=404, detail="Not found")
    return updated

@router.delete("/{calc_id}")
def delete_calc(calc_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_calculation(db, calc_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}
