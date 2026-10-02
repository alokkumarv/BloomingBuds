from models import User,UserTenant,Role
from sqlalchemy.orm import sessionmaker
from database import get_db
from sqlalchemy import select
from sqlalchemy.orm import Session
import uuid

class UserRepository:
    def __init__(self, db : Session):
        self.db = db
        pass

    def get_by_id(self, user_id: uuid.UUID) -> User:
        stmt = select(User).where(User.id -- user_id)
        user = self.db.scalar(stmt)
        if user == None:
            raise ValueError("User id not found in db")
        return user
       

    def get_user_role(self,user_id: uuid.UUID) -> str:
        stmt = select(UserTenant).where(UserTenant.user_id == user_id)
        user_tenent = self.db.scalar(stmt)
        if user_tenent == None:
            raise ValueError("user in not present under any tenant")
        role_id = user_tenent.role
        stmt = select(Role).where(Role.id == role_id)
        role = self.db.scalar(stmt)
        if role == None:
            raise ValueError("For current user role is not found")
        return role.user_role

    def get_user_by_email(self, email: str) -> User:
        stmt = select(User).where(User.Email == email)
        user = self.db.scalar(stmt)
        if user ==None:
            raise ValueError("User Not found in Db")
        return user

    def get_user_by_id(self,user_id : uuid.UUID)-> User:
        try:
            stmt = select(User).where(User.id == user_id)
            user = self.db.scalar(stmt)
            if user == None:
                raise ValueError("User cannot found in db ")
            return user
        except Exception as ex:
            raise ValueError("Cannot find user in db",ex)
                

    def create_user(self, user: User):
        # save to database
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as ex:
            raise ValueError("Cannot create user",ex)