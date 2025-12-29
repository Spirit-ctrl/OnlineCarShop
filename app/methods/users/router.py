from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

import db
from methods.users.hash import get_password_hash
from methods.users import schemas
from methods.users import valid
from methods.users import db_methods

from methods.jwt_auth import jwt1

router_user = APIRouter(tags=["Users"], prefix="/user")


@router_user.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schemas.User, database: Session = Depends(db.get_db)):
    user = await valid.verify_email_exist(email=request.email, db=database)

    if user:
        raise HTTPException(status_code=400, detail="Такой email уже есть в системе")

    new_user = db_methods.user_register(user=request, db=database)

    return new_user


@router_user.get('/', response_model=List[schemas.ViewsUser])
async def get_all_users(database: Session = Depends(db.get_db),
                        current_user: schemas.User = Depends(jwt1.get_current_user)):
    return await db_methods.all_users(database=database)


@router_user.get('/{user_id}', response_model=schemas.ViewsUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                         current_user: schemas.User = Depends(jwt1.get_current_user)):
    return await db_methods.get_user_by_id(user_id=user_id, database=database)


@router_user.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                            current_user: schemas.User = Depends(jwt1.get_current_user)):
    return await db_methods.delete_user_by_id(user_id=user_id, database=database)