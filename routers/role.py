from fastapi import APIRouter,HTTPException,Depends
from services import RoleService
from database import get_db
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

role = APIRouter(prefix="/role",tags=["RolesManagement"])




@role.get("/")
def get_all_roles(db : Session = Depends(get_db)):
    try:
        logger.info("get all roles called ")
        role_service  = RoleService(db=db)
        roles = role_service.get_all_roles()
        return roles
    except Exception as ex:
        raise HTTPException(status_code=404,detail="Cannot get all roles")



