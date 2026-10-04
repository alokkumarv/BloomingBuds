from sqlalchemy.orm import Session
from repository import RoleRepository
import logging

logger = logging.getLogger(__name__)



class RoleService:
    def __init__(self,db : Session):
        self.role_repository = RoleRepository(db=db)

    def get_all_roles(self):
        try:
            result = self.role_repository.get_all_role()
            logger.info("Get role. {}".format(result))
            return result
        except Exception as ex:
            logger.info("Exception occured : {}".format(ex))
            raise            
