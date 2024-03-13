from datetime import datetime, timezone

from jose import jwt
from sqlalchemy.orm import Session

from config import ACCESS_TOKEN_EXPIRE, ALGORITHM, SECRET_KEY
from models import User
from schemas import TokenData
from services.user import get_user_by_email


def create_access_token(user: User):
    to_encode = TokenData(
        sub=user.email,  # type:ignore
        exp=datetime.now(timezone.utc) + ACCESS_TOKEN_EXPIRE
    ).model_dump()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(db: Session, token: str):
    payload = TokenData(**jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]))
    return get_user_by_email(db, payload.sub)
