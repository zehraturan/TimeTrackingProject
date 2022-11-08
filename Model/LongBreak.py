import json

class LongBreak  : 
    duration = 30
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def __getitem__(self, item):
        return getattr(self, item)