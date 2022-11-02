from Model.User import User
from DB.DbAccess import DbAccess

class PomController():
    dbAccess = DbAccess()
    
    def __init__(self, user):
        self.user = user
        
    def addRecipient(self, r_email):
        self.user.addRecipient(r_email)
        self.dbAccess.saveUser(self.user)