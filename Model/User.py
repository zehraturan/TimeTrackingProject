import json

from Model.Project import Project
from Model.Subject import Subject

class User(object):
    def __init__(self, email, name, projects, recipients):
        self.name = name
        self.email = email
        self.projects = projects
        self.recipients = recipients

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def addRecipient(self, r_email):
        if r_email not in self.recipients:
            self.recipients.append(r_email)
            return True
        return False
        
    def addProject(self, p_name):
        if p_name not in self.projects:
            proj=Project(p_name,{})
            self.projects.update({p_name:proj})
            return True
        return False
    
    def getProject(self, p_name):
        return self.projects[p_name]
    
    def addSubject(self, p_name, s_name):
        if s_name not in self.projects[p_name]['subjects']:
            subj = Subject(s_name,[])
            self.projects[p_name]['subjects'][s_name] = subj
            return True
        return False
    
