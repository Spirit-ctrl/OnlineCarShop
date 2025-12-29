import uvicorn

from fastapi import FastAPI
from methods.users.router import router_user
from methods.jwt_auth.router import router_jwt

from db import engine, Base


app = FastAPI(title="First PET Project")

app.include_router(router_user)
app.include_router(router_jwt)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run('main:app', host='127.0.0.2', port=8000, reload=True)
