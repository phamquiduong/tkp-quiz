from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from dependencies.db import get_db
from helpers.token import create_access_token
from schemas import User, UserCreate, UserLogin
from schemas.token import Token
from services.user import authenticate_user, create_teacher, is_exists_user

router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.post('/register', response_model=User, status_code=status.HTTP_201_CREATED)
def register_teacher(
    user_create: UserCreate,
    db: Session = Depends(get_db)
):
    if is_exists_user(db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not permission for create teacher account"
        )

    return create_teacher(db, user_create).__dict__


@router.post("/token", response_model=Token, include_in_schema=False)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token = create_access_token(user)
    return Token(access_token=access_token, token_type="bearer")


@router.post("/login", response_model=Token)
async def login(
    user_login: UserLogin = Body(...),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, user_login.email, user_login.password)
    access_token = create_access_token(user)
    return Token(access_token=access_token, token_type="bearer")
