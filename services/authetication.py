from schemas.schema import  LoginRequest,LoginResponse
from repository.user import UserRepository 
from sqlalchemy.orm import Session 
from .token import generate_token
def login(login_req :LoginRequest, db: Session):
    """Authenticate a user."""
    try:
        user_repo = UserRepository(db=db)
        user = user_repo.get_by_email(login_req.Email)
        if user != None:
            role = user_repo.get_user_role(user.id)
            access_token = generate_token(user=user,role=role)
            return access_token
    except Exception as ex:
        raise ex

def logout(user):
    """End the user's session."""
    pass


def authenticate(token):
    """Validate a token and return the user."""

    pass
