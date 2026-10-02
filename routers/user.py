from fastapi import APIRouter,Depends,HTTPException
from schemas.schema import CreateUserRequest,CreateUserResponse,GetUserResponse
from sqlalchemy.orm import Session
from database.database import get_db
from services.users import UserService
import uuid
import logging


logger = logging.getLogger(__name__)


user = APIRouter(prefix="/users",tags=["UserManagement"])


@user.post("/create",response_model=CreateUserResponse)
def create_user(new_user: CreateUserRequest,db : Session = Depends(get_db)):
    logger.info("create_user ")
    try:
        user_service = UserService(db)
        user = user_service.create_user(new_user=new_user)
        return CreateUserResponse(id=user.id,email=user.Email,created_at=user.CreatedAt)
    except Exception as ex:
        raise HTTPException(status_code=404,detail="Cannot create a new new user {}".format(ex))
        
@user.get("get/:user_id")
def get_user(user_id: uuid.UUID,db : Session = Depends(get_db)):
    logger.info("get_user ")
    try:
        user_service = UserService(db)
        user = user_service.get_user(user_id)
        response = GetUserResponse(id=user["id"],email=user["Email"],first_name=user["FirstName"],last_name=user["LastName"],phone=user["Phone"],role=user["Role"])
        return response
    except Exception as ex:
        print("Exception {}".format(ex))
        raise HTTPException(status_code=404,detail="{}".format(ex))
    
# def update_user(self, user_id: int) -> bool:

@user.delete("/delete")
def delete_user(user_id: uuid.UUID, db : Session = Depends(get_db)):
    logger.info("delete_user ")
    try:
        user_service = UserService(db)
        response = user_service.delete_user(user_id)
        return response
    except Exception as ex:
        raise HTTPException(status_code=404,detail="Not able to delete user {}".format(ex))