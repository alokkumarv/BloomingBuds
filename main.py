from fastapi import FastAPI
from fastapi.security import HTTPBearer
import logging

from routers.authentication import auth as auth_router
from routers.user import user as user_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

bearer_scheme = HTTPBearer()

app.include_router(auth_router)
app.include_router(user_router)

logger.info("App started")
