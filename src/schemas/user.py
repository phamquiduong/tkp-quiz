from pydantic import BaseModel

from schemas import Group


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    group: Group | None

    class Config:
        orm_mode = True
