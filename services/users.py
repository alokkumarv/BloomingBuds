from sqlalchemy.orm import Session
from repository.user import UserRepository
from schemas.schema import CreateUserRequest
from models.user import User
from util.util import sqlalchemy_to_dict
import logging

from models.user import User


class UserService:
    def __init__(self,db: Session):
        self.user_repository = UserRepository(db=db)


    def create_user(self,new_user : CreateUserRequest) -> User:
        try:
            user = User(
                Email=new_user.email,
                PasswordHash=new_user.password_hash,
                FirstName=new_user.first_name,
                LastName=new_user.last_name,
                Phone=new_user.phone,
            )
            user = self.user_repository.create_user(user=user)
            return user
        except Exception as ex:
            raise ValueError("Cannot create new user ",ex)

    def get_user(self,user_id) -> User:
        try:
            user = self.user_repository.get_user_by_id(user_id)
            user_role = self.user_repository.get_user_role(user_id=user.id)
            user = sqlalchemy_to_dict(user)
            user["Role"] = user_role
            return user
        except Exception as ex:
            raise ValueError("Cannot get user in db",ex)
        



