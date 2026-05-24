from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from sqlalchemy.orm import Session

from core.database import get_db
from core.jwt_handler import SECRET_KEY, ALGORITHM

from models.user import User


# TOKEN GET FROM HEADER
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/user/login"
)


# CURRENT LOGIN USER
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:
        # DECODE TOKEN
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # GET USER ID FROM TOKEN
        user_id = payload.get("user_id")

        if not user_id:

            return {
                "message": "Invalid token"
            }

        # FIND USER
        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if not user:

            return {
                "message": "User not found"
            }

        return user

    except JWTError:

        return {
            "message": "Token is invalid"
        } 