from typing import List
from fastapi import APIRouter, status
from fastapi.params import Depends
from app.api.supplier import SupplierSchema, ShowSupplierSchema
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Supplier


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(supplier: SupplierSchema, db: Session = Depends(get_db)): 
    db.add(Supplier(**supplier.dict())) 
    db.commit()


@router.get('/', response_model=List[ShowSupplierSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Supplier).all()


@router.put('/{id}')
def update(id: int, supplier: SupplierSchema, db: Session = Depends(get_db)):
    query = db.query(Supplier).filter_by(id=id) 
    query.update(supplier.dict())
    db.commit()


@router.get('/{id}', response_model=ShowSupplierSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Supplier).filter_by(id=id).first()