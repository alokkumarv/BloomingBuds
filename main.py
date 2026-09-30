from fastapi import FastAPI
from schema import CreateTenantRequest,CreateTenantResponse,CreateUserRequest,CreateUserResponse,LoginRequest,LoginResponse
import uuid
from services import Services
app = FastAPI()

services = Services()



@app.post("/login")
async def login(req :LoginRequest):
    print("Email : ",req.Email)
    print("Password : ",req.Password)
    user = services.validate_login(req.Email,req.Password)
    token = services.create_jwt_token(user)
    if user != None:
        return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.post("/create_tenant", response_model=CreateTenantResponse)
async def create_tenant(tenant: CreateTenantRequest):
    print(tenant.name)
    tenant = {
        "id": uuid.uuid1(),
        "name": tenant.name
    }
    return tenant

@app.post("/create_user",response_model=CreateUserResponse)
async def create_user(user : CreateUserRequest):
    user = {
            "id": uuid.uuid1(),
            "email": user.email
        }
    return user

