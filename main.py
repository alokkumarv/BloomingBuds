from fastapi import FastAPI
from fastapi.security import HTTPBearer
import logging


from routers import tenant_router,auth_router,user_router,role_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

bearer_scheme = HTTPBearer()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(tenant_router)
app.include_router(role_router)


logger.info("App started")
