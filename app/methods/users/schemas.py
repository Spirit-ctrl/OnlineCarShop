from pydantic import BaseModel, Field, EmailStr, conlist, field_validator, ConfigDict
from typing import  Literal
import re

class User(BaseModel):
    first_name: str =  Field(min_length=1, max_length=12)
    last_name: str = Field(min_length=1, max_length=12)
    sex: str =  conlist(Literal["male", "woman"])
    age: int = Field(ge=18, le=99)
    login : str
    email: EmailStr
    password: str
    phone_number:str

    @field_validator("phone_number", mode="plain")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(r'^\+\d{5,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 5 до 15 цифр')
        return value
    

class ViewsUser(BaseModel):

    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)