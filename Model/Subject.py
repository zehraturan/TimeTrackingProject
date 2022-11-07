import json

class Subject:
    def __init__(self, name, pomodoro_list):
        self.name = name   
        self.pomodoro_list = []    
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    