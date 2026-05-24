from passlib.context import CryptContext 
# cryptContext hash me convert krta hai 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#create a pwd_context & bcrypt hashing algorithm

def hash_password(password: str):
    return pwd_context.hash(password)
#create hsh password

def verify_password(
    plain_password,
    hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
#verify password