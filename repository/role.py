from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
import util
from models import Role
import logging

logger = logging.getLogger(__name__)
import uuid 


class RoleRepository:
    def __init__(self,db : Session):
        self.db = db

    def get_all_role(self):
        try:
            stmt = select(Role)
            result = self.db.execute(statement=stmt)
            roles = result.scalars().all()
            logger.info(roles)
            roles = [util.sql_model_to_dict(role) for role in roles]
            logger.info(roles)
            return roles
        except SQLAlchemyError as ex:
            logging.info("Exception occured while getting all roles : {}".format(ex))


    def get_role_by_id(self,role_id : uuid.UUID):
        
        pass

    def create_new_role(self,role_name : str):
        pass