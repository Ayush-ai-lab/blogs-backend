from fastapi import APIRouter
from schemas.user_schema import RegisterSchema, LoginSchema
from services.user_service import register, user_update, get_all_user, get_single_user, user_delete, login
from sqlalchemy.orm import Session
from core.database import get_db
from fastapi import Depends

router = APIRouter(
        prefix="/user",
        tags=["user"])

@router.post("/register")
def Register(user: RegisterSchema, db: Session = Depends(get_db)):
        return register(user, db)

@router.post("/login")
def Login(user: LoginSchema,db: Session = Depends(get_db)):
         return login(user, db)

@router.put("/update-user/{id}")
def UpdateUser(id: int, user: RegisterSchema, db: Session = Depends(get_db)):
        return user_update(id, user, db)

@router.get("/")
def GetUsers(db: Session = Depends(get_db)):
        return get_all_user(db)

@router.get("/single-user/{id}")
def GetSingleUser(id: int, db: Session = Depends(get_db)):
        return get_single_user(id, db)

@router.delete("/delete-user/{id}")
def DeleteUser(id:int, db: Session = Depends(get_db)):
        return user_delete(id, db)