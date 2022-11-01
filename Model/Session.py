import json


class Session:
    duration = 25

    def __init__(self, name, task_list=[]):
        self.name = name
        self.task_list = task_list

    def addTask(self, task):
        self.task_list.append(task)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
