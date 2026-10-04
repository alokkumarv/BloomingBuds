from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound,NoResultFound,SQLAlchemyError
from models import Tenant
import util
import uuid
import logging


logger = logging.getLogger(__name__)

class TenantRepository:
    def __init__(self,db : Session):
        self.db = db
    def get_tenant_by_id(self,tenant_id : uuid.UUID):
        logger.info("Get tenant by is called ")
        try:
            stmt = select(Tenant).where(Tenant.id == tenant_id)
            tenant = util.sqlalchemy_to_dict(self.db.execute(stmt).scalar_one())
            return tenant
        except MultipleResultsFound as ex:
            logger.info("Exception occured : {}".format(ex))
            raise ValueError("Multiple tenant avaliable with this id ")
        except NoResultFound as ex:
            logger.info("Exception occured : {}".format(ex))
            raise ValueError("Tenant with this id does not exist")
        
    def create_new_tenant(self,new_tenant : dict):
        try:
            logger.info("Create new tenent called")
            new_tenant  = util.dict_to_model(Tenant,new_tenant)
            logger.info(new_tenant)
            self.db.add(new_tenant)
            self.db.commit()
            self.db.refresh(new_tenant)
            logger.info("new tenant {}".format(new_tenant))
            new_tenant = util.sql_model_to_dict(new_tenant)
            return new_tenant
        
        except SQLAlchemyError as ex:
            logger.info("Exception occured : {}".format(ex))
            self.db.rollback()
            
            raise