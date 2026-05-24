from fastapi import APIRouter
from schemas.user_schema import RegisterSchema, LoginSchema
from services.user_service import create_user, update_user, get_all_user, get_single_user, delete_user, login
from sqlalchemy.orm import session
from core.database import get_db
from fastapi import Depends

router = APIRouter(
        prefix="/user",
        tags=["user"])

@router.post("/register")
def Register(user: RegisterSchema):
        

        return {
            "message": "User create successfully",
            "data": user
        }

@router.post("/login")
def Login(user: LoginSchema):
        return {"message": "User login successfully",
                "data": user
        }

@router.put("/update-user/{id}")
def update_user(id: int, user: RegisterSchema):
        return update_user(id, user     )

@router.get("/")
def get_all_user():
        return get_all_user()

@router.get("/single-user/{id}")
def get_single_user(id: int):
        return get_single_user(id)

@router.delete("/delete-user/{id}")
def delete_user(id:int):
        return delete_user(id)