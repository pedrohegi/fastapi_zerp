from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    """
    Esse é um contrato de entrada
    """

    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    """
    Esse é um contrato de saída
    """

    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]
