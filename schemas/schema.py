from datetime import datetime
from enum import Enum
from pydantic import BaseModel,Field,EmailStr,ConfigDict
import uuid


class LoginRequest(BaseModel):
        Email : str = Field(EmailStr)
        Password : str = Field(str)

class LoginResponse(BaseModel):
        ResponseStatus : int
        ResponseMessage : str


class LoginTokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class CreateTenantRequest(BaseModel):
        name : str = Field(max_length=50)
        email : str = Field(EmailStr)
        phone  : str = Field(max_length=13)
        address : str = Field(max_length=100)
        country : str = Field(max_length=50)

class CreateTenantResponse(BaseModel):
        id : uuid.UUID 
        name : str
        

class CreateUserRequest(BaseModel):
        email: str = Field(EmailStr)
        password_hash: str = Field(min_length=4)
        first_name: str = Field(max_length=40)
        last_name: str = Field(max_length=40)
        phone: str = Field(max_length=13)
        role: str | None = None


class CreateUserResponse(BaseModel):
        id: uuid.UUID
        email: EmailStr
        created_at: datetime

class GetUserResponse(BaseModel):
        id: uuid.UUID
        email: str = Field(EmailStr)
        first_name: str = Field(max_length=40)
        last_name: str = Field(max_length=40)
        phone: str = Field()
        role: str | None = None
       