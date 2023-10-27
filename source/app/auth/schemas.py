from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class Credentials(BaseModel):
    username: str
    password: str


class Refresh(BaseModel):
    refresh_token: str
