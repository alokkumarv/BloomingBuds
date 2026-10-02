from fastapi import FastAPI
from routers import auth,user
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()


app.include_router(router=auth)
app.include_router(router=user)


if __name__ == "__main__":
    pass