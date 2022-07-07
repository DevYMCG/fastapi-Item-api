from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from v1.service import item_service
from v1.schema import item_schema
from v1.schema.user_schema import User
from v1.service.auth_service import get_current_user

from v1.utils.database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/api/v1")


@router.post(
    "/users/items/",
    tags=["items"],
    response_model=item_schema.Item)
def create_item_for_user(
    item: item_schema.ItemCreate, db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return item_service.create_user_item(db=db, item=item, user=current_user)


@router.get(
    "/items/",
    tags=["items"],
    response_model=List[item_schema.Item]
)
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_service.get_items(db, skip=skip, limit=limit)
    return items