from sqlalchemy.orm import Session
from app import models
from app.schemas.user import UserCreate
from app.schemas.calculation import CalculationCreate
from app.security import hash_password, verify_password



def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: UserCreate):
    if not isinstance(user.password, str):
        raise ValueError("password must be a string")

    hashed = hash_password(user.password)
    db_user = models.User(username=user.username, email=user.email, password_hash=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user


def create_calculation(db: Session, calc: CalculationCreate):
    db_calc = models.Calculation(expression=calc.expression, result=calc.result)
    db.add(db_calc)
    db.commit()
    db.refresh(db_calc)
    return db_calc

def get_calculation(db: Session, calc_id: int):
    return db.query(models.Calculation).filter(models.Calculation.id == calc_id).first()

def list_calculations(db: Session):
    return db.query(models.Calculation).all()

def update_calculation(db: Session, calc_id: int, values: dict):
    calc = get_calculation(db, calc_id)
    if not calc:
        return None
    for k, v in values.items():
        setattr(calc, k, v)
    db.commit()
    db.refresh(calc)
    return calc

def delete_calculation(db: Session, calc_id: int):
    calc = get_calculation(db, calc_id)
    if not calc:
        return False
    db.delete(calc)
    db.commit()
    return True
