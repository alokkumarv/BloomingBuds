from fastapi import APIRouter,Depends,HTTPException
from schemas.schema import CreateUserRequest,CreateUserResponse,GetUserResponse
from sqlalchemy.orm import Session
from database import get_db
import services
from services.users import UserService
import uuid


user = APIRouter(prefix="/users",tags=["UserManagement"])


@user.post("/create",response_model=CreateUserResponse)
def create_user(new_user: CreateUserRequest,db : Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        user = user_service.create_user(new_user=new_user)
        return CreateUserResponse(id=user.id,email=user.Email,created_at=user.CreatedAt)
    except Exception as ex:
        raise HTTPException(status_code=404,detail="Cannot create a new new user {}".format(ex))
        
@user.get("/:user_id")
def get_user(user_id: uuid.UUID,db : Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        user = user_service.get_user(user_id)
        response = GetUserResponse(id=user["id"],email=user["Email"],first_name=user["FirstName"],last_name=user["LastName"],phone=user["Phone"],role=user["Role"])
        return response
    except Exception as ex:
        raise HTTPException(status_code=404,detail="{}".format(ex))
    
# def update_user(self, user_id: int) -> bool:
# def delete_user(self, user_id: int) -> bool: