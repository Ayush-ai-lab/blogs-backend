from models.user import User 
from core.security import hash_password, verify_password
from core.jwt_handler import create_access_token


def register(user, db):
    # hash_pass = hash_password(password)
    hash_pass = hash_password(user.password)
    new_user = User(
        name = user.name,
        email = user.email,
        password =  hash_pass
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message" : "User register Successfully",
        "data" : new_user
    }

def login(user, id):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()
    # find the user

    if not db_user:
        return {
            "message": "Invalid email"
        }
    #user not found
    password_match = verify_password(
        user.password,
        db_user.password
    )
    
    #check the password

    if not password_match:
        return {
            "message": "Invalid password"
        }
    # if in valid password

    access_token = create_access_token(
        data={
            "user_id": db_user.id,
            "email": db_user.email
        }
    )
    #access token created

    return {
        "message": "User login successfully",
        "access_token" : access_token
    }


def user_update(updated_user,db,id):
    old_user = db.query(User).filter(User.id == id).first()
    if not old_user:
        return {
            "message" : "No User Found" 
        }
    
    old_user.name = updated_user.name
    old_user.email = updated_user.email
    old_user.password = hash_password(
    updated_user.password
)

    db.commit()
    db.refresh(old_user)
    return {
        "message": "User update successfully"
    }

def user_delete(db,id):
    user = db.query(User).filter(User.id == id).first()

    if not user :
        return {
            "message": "No User Found"
        }
    db.delete(user)
    db.commit()
    return {
        "message": "User delete successfully"
    }

def get_single_user(db,id):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        return {
            "message": "User Not Found "
        }
    return {
        "message": "user fetch successfully",
        "data": user
    }

def get_all_user(db):
        users = db.query(User).all()
        if not users :
            return {
                "message": "Users not found"
            }

        return {
            "message": "User fetch successfully",
            "data": users
        }