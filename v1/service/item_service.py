from sqlalchemy.orm import Session

from v1.model.item_model import Item as ItemModel
from v1.schema import item_schema
from v1.schema import user_schema


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ItemModel).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: item_schema.ItemCreate, user: user_schema.User):

    db_item = ItemModel(
        **item.dict(),
        owner_id=user.id
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item