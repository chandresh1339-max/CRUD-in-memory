import logging
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    id: int = Field(gt=0, description="User ID must be a positive integer")
    name: str = Field(
        min_length=2,
        max_length=50,
        description="Name must be between 2 and 50 characters",
    )
    email: EmailStr = Field(description="Must be a valid email address format")


class UserUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=50,
        description="Name must be between 2 and 50 characters",
    )
    email: Optional[EmailStr] = None


class UserResponse(BaseModel):
    """Schema for uniform, validated outbound data representation."""

    user_id: int
    name: str
    email: EmailStr


# Simple In-Memory Database
db: dict[int, UserResponse] = {}

logger = logging.getLogger("crud")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.FileHandler("logs.txt")
    _handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(_handler)


def create_user(id: int, name: str, email: EmailStr) -> UserResponse:
    user_data = UserCreate(id=id, name=name, email=email)
    if user_data.id in db:
        raise ValueError(f"User with ID {user_data.id} already exists.")
    user_response = UserResponse(
        user_id=user_data.id, name=user_data.name, email=user_data.email
    )
    db[user_data.id] = user_response
    logger.info(
        f"User created: id={user_data.id}, name={user_data.name}, email={user_data.email}"
    )
    return user_response


def read_user(user_id: int) -> UserResponse:
    if user_id not in db:
        raise KeyError(f"User with ID {user_id} not found.")
    return db[user_id]


def update_user(
    user_id: int, name: Optional[str] = None, email: Optional[EmailStr] = None
) -> UserResponse:
    if user_id not in db:
        raise KeyError(f"User with ID {user_id} not found.")

    update_data = UserUpdate(name=name, email=email)
    if update_data.name is not None:
        db[user_id] = db[user_id].copy(update={"name": update_data.name})
    if update_data.email is not None:
        db[user_id] = db[user_id].copy(update={"email": update_data.email})
    return db[user_id]


def delete_user(user_id: int) -> str:
    if user_id not in db:
        raise KeyError(f"User with ID {user_id} not found.")
    del db[user_id]
    return f"User {user_id} deleted successfully."
