from fastapi import APIRouter
from schemas.user_schema import RegisterSchema, LoginSchema

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