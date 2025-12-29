from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import db
from methods.users import hash
from methods.users.models import User
from methods.jwt_auth import jwt1



router_jwt = APIRouter(tags=['Authentication'])


@router_jwt.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(db.get_db)):
    user = database.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")

    if not hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password!")

    access_token = jwt1.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}