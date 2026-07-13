from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

from crud import create_user, read_user, update_user, delete_user, db

app = FastAPI(title="CRUD API")


class UserCreate(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class User(BaseModel):
    name: str
    email: EmailStr


@app.post("/users", response_model=User, status_code=201)
def create_user_endpoint(user: UserCreate):
    try:
        return create_user(user.id, user.name, user.email)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))


@app.get("/users", response_model=dict[int, User])
def list_users_endpoint():
    return db


@app.get("/users/{user_id}", response_model=User)
def read_user_endpoint(user_id: int):
    try:
        return read_user(user_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@app.put("/users/{user_id}", response_model=User)
def update_user_endpoint(user_id: int, user: UserUpdate):
    try:
        return update_user(user_id, name=user.name, email=user.email)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int):
    try:
        return {"message": delete_user(user_id)}
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
