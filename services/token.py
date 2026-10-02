from models import User
from datetime import datetime,timedelta,timezone
import jwt
import os
import json

JWT_SECRET_KEY = "some randome key big number ghjgascascasda"
def generate_token(user : User,role : str):
    """Generate an authentication token."""
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user.id),
        "role": role,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=30)).timestamp()),
    }
    print(type(JWT_SECRET_KEY))
    access_token = jwt.encode(payload=payload,key=JWT_SECRET_KEY,algorithm="HS256")
    return access_token


def refresh_token(refresh_token):
    """Generate a new access token."""
    pass


def verify_token(token):
    """Check whether a token is valid."""
    pass
