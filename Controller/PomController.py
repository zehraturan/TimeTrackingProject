from Model.User import User
from DB.DbAccess import DbAccess
import re

from Model.Project import Project


class PomController():
    dbAccess = DbAccess()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def __init__(self, user):
        self.user = user
        
    def addRecipient(self, r_email):
        if(re.fullmatch(self.regex, r_email)):
            if (self.user.addRecipient(r_email)):
                self.dbAccess.saveUser(self.user)
                return "Success"
        return "Fail"
        
    def getRecipients(self):
        return self.user.recipients
    
    def addProject(self,p_name):
        if p_name.strip():
            if self.user.addProject(p_name):
                self.dbAccess.saveUser(self.user)
                return "Success"
        return "Fail"
    
    def getProjects(self):
        return self.user.projects
    
    def addSubject(self, p_name, s_name):
        if s_name.strip():
            if self.user.addSubject(p_name, s_name):
                print(self.user.toJSON())
                self.dbAccess.saveUser(self.user)
                print(self.user.toJSON())
                return "Success"
        return "Fail"
    
    def getSubjects(self, p_name):
        return self.user.projects[p_name].subjects
    
    def firstProjectSubjects(self):
        if len(self.user.projects) > 0 :
            first_proj = list(self.user.projects.items())[0]
            print('FirstProj')
            print(type(first_proj))

            print(first_proj.toJSON())
            return first_proj.subjects.keys()
        else:
            return list("")
        
        