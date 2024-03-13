from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from helpers.password import get_password_hash, verify_password
from models import User as UserModel
from schemas import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def is_exists_user(db: Session):
    return db.query(UserModel).first() is not None


def create_user(db: Session, user_create: UserCreate, is_teacher: bool = False):
    password = get_password_hash(user_create.password)
    user_db = UserModel(email=user_create.email, password=password, is_teacher=is_teacher)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


def create_teacher(db: Session, user_create: UserCreate):
    return create_user(db, user_create, is_teacher=True)


def authenticate_user(db: Session, email: str, password: str):
    authenticate_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_db = get_user_by_email(db, email)

    if user_db is None:
        authenticate_exception.detail = 'Email does not exist'
        raise authenticate_exception

    if not verify_password(plain_password=password, hashed_password=user_db.password):  # type: ignore
        authenticate_exception.detail = 'Password incorrect'
        raise authenticate_exception

    return user_db
