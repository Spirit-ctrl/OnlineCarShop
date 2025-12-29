from fastapi import HTTPException, status
from methods.users import schemas
from sqlalchemy.orm import Session
from methods.users import models

from typing import List, Optional

def user_register(user: schemas.User, db: Session) -> models.User:
    new_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        sex=user.sex,
        age=user.age,
        email=user.email,
        phone_number=user.phone_number,

        password=user.password,
        login=user.login
    )

    db.add(new_user)
    db.commit()
    return new_user



async def all_users(database: Session) -> List[schemas.ViewsUser]:
    users = database.query(models.User).all()
    return users


async def get_user_by_id(user_id: int, database: Session) -> Optional[models.User]:
    
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден")
    return user_info


async def delete_user_by_id(user_id: int, database: Session) -> None:
    
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()