import json

class ShortBreak  : 
    duration = 5
    
    def __init__(self,name):
        self.name = name
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)