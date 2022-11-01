import json

class Task:
    def __init__(self, name, done):
        self.name = name
        self.done = done
        
def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    