import uuid
from datetime import datetime
from enum import Enum
from pydantic import BaseModel,Field,EmailStr
import uuid


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

class CreateUserResponse(BaseModel):
        id: uuid.UUID 
        email: str 