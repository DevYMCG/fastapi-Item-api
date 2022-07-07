from sqlalchemy.orm import Session

from fastapi import HTTPException, status


from v1.model.user_model import User as UserModel
from v1.schema import user_schema
from v1.service.auth_service import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    get_user = get_user_by_email(db, email=user.email)
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        email=user.email,
        username=user.username,
        hashed_password=get_password_hash(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user