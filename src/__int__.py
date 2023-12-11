from .config import DBConnection
from .entities import Users as UsersModel

class UserRepo:
    def insert_user(self, name):
        with DBConnection as db:
            new_users = UsersModel(name=name)
            db.session.add(new_users)
            db.session.comit()