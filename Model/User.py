import json

class User:
    def __init__(self, email, name, projects=[], recipients=[]):
        self.name = name
        self.email = email
        self.projects = projects
        self.recipients = recipients
        
    def __init__(self, j):
        self.__dict__ = json.loads(j)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
