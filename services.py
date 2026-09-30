import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from Model import User,UserTenant,Role
import jwt
class Services:
    
    def __init__(self):
        DATABASE_URL = os.getenv('DATABASE_URL')
        self.SECRET_KEY = "change-this-to-a-long-random-secret"
        self.ALGORITHM = "HS256"
        self.engine = create_engine(DATABASE_URL)

    def validate_login(self,email : str,password : str):
        with Session(self.engine) as session:
            stmt = select(User).where(User.Email == email)
            result = session.execute(stmt)
            user = result.scalar_one_or_none()
            if user:
                return user
            else:
                return None

    def create_jwt_token(self,user: User):
        token = None
        with Session(self.engine) as session:
            stmt  = select(UserTenant).where(UserTenant.user_id == user.id)
            result = session.execute(stmt)
            use_tenant = result.scalar_one_or_none()
            print(use_tenant.role)
            stmt = select(Role).where(Role.id == use_tenant.role)
            result = session.execute(stmt)
            role = result.scalar_one_or_none()
            print(role.user_role)
            token = {"Email": user.Email,"role": role.user_role}
            token  = jwt.encode(
                token,
                self.SECRET_KEY,
                algorithm=self.ALGORITHM,
    )
            

        return token



