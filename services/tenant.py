from sqlalchemy.orm import Session
from repository import TenantRepository
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
