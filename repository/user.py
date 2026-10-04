from models import User,UserTenant,Role
from sqlalchemy.exc import SQLAlchemyError,MultipleResultsFound,NoResultFound
from sqlalchemy import select,delete
from sqlalchemy.orm import Session
import uuid
import logging
logger = logging.getLogger(__name__)


class UserRepository:
    def __init__(self, db : Session):
        self.db = db
        pass

    def get_by_id(self, user_id: uuid.UUID) -> User:
        try:
            stmt = select(User).where(User.id == user_id)
            user = self.db.execute(stmt).scalar_one()
            if user == None:
                raise ValueError("User id not found in db")
            return user
        except MultipleResultsFound as ex:
            raise ValueError("Multiple user found id not found in db")

    def get_user_role(self,user_id: uuid.UUID) -> str:
        try:
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
        except Exception as ex:
            raise ValueError("Role of user cannot be found ",ex)
        
    def get_user_by_email(self, email: str) -> User:
        try:
            stmt = select(User).where(User.Email == email)
            user = self.db.execute(stmt).scalar_one()
            if user ==None:
                raise ValueError("User Not found in Db")
            return user
        except NoResultFound as ex:
            raise ValueError("User Not found in Db ",ex)
        except MultipleResultsFound as ex:
            raise ValueError("Multiple user found in db ",ex)
        
    def get_user_by_id(self,user_id : uuid.UUID)-> User:
        try:
            stmt = select(User).where(User.id == user_id)
            user = self.db.scalar(stmt)
            if user == None:
                raise ValueError("User cannot found in db ")
            return user
        except SQLAlchemyError as ex:
            raise ValueError("Cannot find user in db",ex)
                

    def create_user(self, user: User):
        # save to database
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except SQLAlchemyError as ex:
            raise ValueError("Cannot create user",ex)
    def delete_user_by_id(self,user_id: uuid.UUID):
        logger.info("delete_user_by_id")
        try:
            stmt = delete(User).where(User.id == user_id)
            logger.info("statement created")

            result = self.db.execute(stmt)
            logger.info("statement executed: %s", result)

            self.db.commit()
            logger.info("commit successful")
        except SQLAlchemyError as ex:
            self.db.rollback()
            logger.exception("Failed to delete user %s", user_id)
            raise 