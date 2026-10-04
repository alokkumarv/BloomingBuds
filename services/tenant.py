from sqlalchemy.orm import Session
from repository import TenantRepository
import uuid
import logging

loggger = logging.getLogger(__name__)

class TenantService:

    def __init__(self,db: Session):
        self.tenant_repository = TenantRepository(db=db)

    def create_new_tenant(self,new_tenant : dict):
        try:
            result = self.tenant_repository.create_new_tenant(new_tenant=new_tenant)
            loggger.info("")
            return result
        except Exception as ex: 
            loggger.info("Exception occured while creating a new tenant :{}".format(ex))
            raise
    def get_tenant_by_id(self,tenant_id: uuid.UUID):
        try:
            result = self.tenant_repository.get_tenant_by_id(tenant_id=tenant_id)
            return result
        except Exception as ex:
            loggger.info("Exception occureed : {}".format(ex))
            raise