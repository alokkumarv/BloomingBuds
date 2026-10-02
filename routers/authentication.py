from fastapi import APIRouter,Depends,HTTPException
from schemas.schema import LoginRequest,LoginTokenResponse
import services.authetication as authservice
from sqlalchemy.orm import Session
from database import get_db
auth = APIRouter(prefix='/auth',tags=["Authetication"])


@auth.post("/login",response_model=LoginTokenResponse)
async def login(login_req :LoginRequest, db : Session = Depends(get_db)):
    """Authenticate a user."""
    try:
        access_token = authservice.login(login_req,db)
        return LoginTokenResponse(access_token=access_token)
    except Exception as ex:
        raise HTTPException(status_code=404,detail="Cannot generate token")

def logout(user):
    """End the user's session."""
    pass


def authenticate(token):
    """Validate a token and return the user."""
    pass


def generate_token(user):
    """Generate an authentication token."""
    pass


def refresh_token(refresh_token):
    """Generate a new access token."""
    pass


def verify_token(token):
    """Check whether a token is valid."""
    pass


def get_current_user(token):
    """Get the authenticated user from a token."""
    pass


def has_permission(user, permission):
    """Check whether a user has a specific permission."""
    pass
