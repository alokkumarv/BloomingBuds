from fastapi import FastAPI
from schema import CreateTenantRequest,CreateTenantResponse,CreateUserRequest,CreateUserResponse
import uuid
app = FastAPI()





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

