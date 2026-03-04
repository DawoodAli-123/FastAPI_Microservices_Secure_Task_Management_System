from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    role: str = "user"

class Token(BaseModel):
    access_token: str
    token_type: str
