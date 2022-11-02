import json

class User(object):
    def __init__(self, email, name, projects=[], recipients=[]):
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
            self.projects.append(p_name)
            return True
        return False
        
    
        
    
