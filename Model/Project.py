import json

class Project  : 
    def __init__ ( self, name, subject_list=[]):
        self.name = name
        self.subject_list=subject_list
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)