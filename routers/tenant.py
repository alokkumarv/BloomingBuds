from fastapi import APIRouter,Depends,HTTPException
from schemas import CreateTenantResponse,CreateTenantRequest
from sqlalchemy.orm import Session
from database import get_db
from services import TenantService
import uuid
import logging
import util

logger = logging.getLogger(__name__)


tenant = APIRouter(prefix="/tenant",tags=["TenantsManagement"])

@tenant.post("/create",response_model=CreateTenantResponse)
def create_new_tenant(tenant : CreateTenantRequest,db :Session =  Depends(get_db)):
    try:
        logger.info("Create new tenant called {}".format(tenant))
        new_tenant = tenant.model_dump()
        logger.info("New tenant createtion {}".format(new_tenant))
        tenant_Service = TenantService(db=db)
        result = tenant_Service.create_new_tenant(new_tenant=new_tenant)
        logger.info("result : {}".format(result))
        return CreateTenantResponse(id=result['id'],name=result['Name'])
    except Exception as ex:
        raise HTTPException(status_code=422,detail="Cannot create a tenant ")


@tenant.get("/")
def get_tenant_by_id(id : uuid.UUID , db:  Session =Depends(get_db)):
    try:
        logger.info("get tenant api called for : {}".format(id))
        pass
    except Exception as ex:
        raise HTTPException(status_code=404 ,detail="Tenant not found ")


    
