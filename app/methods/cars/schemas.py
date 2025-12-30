from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class Category(BaseModel):
    name: str = Field(min_length=1, max_length=50)


class DisplayCategory(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class CarBase(BaseModel):
    id: Optional[int]
    name: str
    quantity: int
    description: str
    price: float

    model_config = ConfigDict(from_attributes=True)


class Car(CarBase):
    category_id: int


class DisplayCar(CarBase):
    category: DisplayCategory

    model_config = ConfigDict(from_attributes=True)


class CarCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    quantity: int
    description: str
    price: float
    category_id: int