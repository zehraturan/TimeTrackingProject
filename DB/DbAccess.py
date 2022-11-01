from collections import UserDict
import json
import os.path

from Model.User import User

class DbAccess:
    json_file = 'new.json'
    userDict = dict()

    def __init__(self):
        self.userDict = self.read()

    def saveUser(self,user):
        self.userDict.update({user.email : user.toJSON()})
        self.write(self.userDict)

    def getUser(self,email):
        return User(self.userDict.get(email))
        
    def isExistUser(self, email):
        if email in self.userDict:
            return True
        else:
            return False

    def write(self, whole_data):  # re-write our updated dictionary

        with open(self.json_file, "w") as file:
            json.dump(whole_data, file)

    def read(self):  # return a python dict
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as file:
                if file.read() != '':
                    file.seek(0)
                    return json.loads(file.read())
            
        return {}
