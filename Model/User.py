import json

class User  : 
    def __init__ ( self, email,name):
        #self.data = dicti.get (email)
        self.name = name
        self.email = email
        #self.name=self.data.get('name')
        #self.projects= self.data.get('projects')
        #self.recipients=self.data.get('recipients')
#         self.subjects= list(self.data.get('projects').keys())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
