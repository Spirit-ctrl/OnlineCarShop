from sqlalchemy.orm import Session
from typing import Optional
from pydantic import EmailStr
from methods.users.models import User


async def verify_email_exist(email: EmailStr, db: Session) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()