from db import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)

    first_name = Column(String, default = None)
    last_name = Column(String, default = None)
    sex = Column(String)
    age = Column(String, nullable=True)
    email = Column(String, default = None, unique=True)
    phone_number = Column(String, default=None, unique=True, nullable=True)

    password = Column(String, nullable=True)
    login = Column(String, nullable=True)


    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)

    

