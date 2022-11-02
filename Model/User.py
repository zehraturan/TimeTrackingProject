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
        self.recipients.append(r_email)
        
    
        
    
