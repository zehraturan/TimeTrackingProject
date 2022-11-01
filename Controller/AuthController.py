from collections import UserDict

from Model.User import User
from DB.DbAccess import DbAccess

class AuthController :
    dbAccess = DbAccess()
    
    def login(self,email):
        #user = User(email)
        if self.dbAccess.isExistUser(email):
            return "Success"
        else:
            return "User not found"

    def signup(self, name, email):
        if self.dbAccess.isExistUser(email):
            return "Already exist"
        else:
            user = User(name, email)
            self.dbAccess.saveUser(user)
            return "Success"