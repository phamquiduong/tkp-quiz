from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from database import SessionLocal
from helpers.token import get_current_user as get_current_user_from_token
from models import User as UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Bearer"},
    )

    db = SessionLocal()

    try:
        user = get_current_user_from_token(db=db, token=token)
    except JWTError as jwt_error:
        credentials_exception.detail = str(jwt_error)
        raise credentials_exception from jwt_error

    if user is None:
        credentials_exception.detail = 'User does not exist'
        raise credentials_exception

    return user


async def get_current_teacher(
    current_user: Annotated[UserModel, Depends(get_current_user)]
):
    if not current_user.is_teacher:  # type:ignore
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not teacher")
    return current_user
