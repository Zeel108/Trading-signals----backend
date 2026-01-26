from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "SECRET123"   # later move to env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_crypt_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_crypt_context.verify(password, hashed)

def create_access_token(data: dict):
    encode_pass = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode_pass.update({"exp": expire})
    return jwt.encode(encode_pass, SECRET_KEY, algorithm=ALGORITHM)
