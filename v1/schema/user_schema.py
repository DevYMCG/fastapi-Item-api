from typing import List

from pydantic import BaseModel

from v1.schema import item_schema

class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[item_schema.Item] = []

    class Config:
        orm_mode = True