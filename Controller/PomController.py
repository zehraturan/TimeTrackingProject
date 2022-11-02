from Model.User import User
from DB.DbAccess import DbAccess
import re


class PomController():
    dbAccess = DbAccess()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def __init__(self, user):
        self.user = user
        
    def addRecipient(self, r_email):
        if(re.fullmatch(self.regex, r_email)):
            self.user.addRecipient(r_email)
            self.dbAccess.saveUser(self.user)
            return "Success"
        return "Fail"
        
    def getRecipients(self):
        return self.user.recipients