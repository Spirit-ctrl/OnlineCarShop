from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from app.methods.jwt_auth import router
import db
from . import shema, services, validator

router_cars = APIRouter(tags=["Categories & cars"], prefix="/cars")


@router_cars.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: shema.Category, database: Session = Depends(db.get_db)):
    new_category = await services.create_new_category(request, database)
    return new_category


@router_cars.get('/category', response_model=List[shema.DisplayCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    categories = await services.get_all_categories(database)
    return categories


@router_cars.get('/category/{category_id}', response_model=shema.DisplayCategory)
async def get_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    category = await services.get_category_by_id(category_id, database)
    return category


@router_cars.delete('/category/{category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_category(category_id: int, database: Session = Depends(db.get_db)) -> None:
    return await services.delete_category_by_id(category_id, database)


@router_cars.post('/', status_code=status.HTTP_201_CREATED, response_model=shema.DisplayCar)
async def create_car(request: shema.CarCreate, database: Session = Depends(db.get_db)):
    category = await validator.verify_category_exist(request.category_id, database)
    if not category:
        raise HTTPException(status_code=404, detail="You have provided invalid category id!")
    new_car = await services.create_new_car(request, database)
    return new_car


@router_cars.get('/', response_model=List[shema.DisplayCar])
async def get_all_cars(database: Session = Depends(db.get_db)):
    cars = await services.get_all_cars(database)
    return cars


@router_cars.get('/{car_id}', response_model=shema.DisplayCar)
async def get_car_by_id(car_id: int, database: Session = Depends(db.get_db)):
    car = await services.get_car_by_id(car_id, database)
    return car


@router_cars.delete('/{car_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_car(car_id: int, database: Session = Depends(db.get_db)) -> None:
    return await services.delete_car_by_id(car_id, database)