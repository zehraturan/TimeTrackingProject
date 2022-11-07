import json

from Model.Subject import Subject

class Project(object)  : 
    def __init__ ( self, name, subjects):
        self.name = name
        self.subjects={}
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    