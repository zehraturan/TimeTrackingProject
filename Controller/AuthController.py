from Model.User import User
from DB.DbAccess import DbAccess
import re

class AuthController :
    dbAccess = DbAccess()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    def login(self,email):
        if self.dbAccess.isExistUser(email):
            self.current_user = self.dbAccess.getUser(email)
            return "Success"
        else:
            return "User not found"

    def signup(self, email, name):
        if self.dbAccess.isExistUser(email):
            return "Already exist"
        elif(re.fullmatch(self.regex, email)):
            user = User(email, name,{},[])
            self.dbAccess.saveUser(user)
            return "Success"
        else:
            return "Fail"
        