import json


class Session:
    duration = 25

    def __init__(self, name, start_time=None, finish_time=None):
        self.name = name
        self.start_time = start_time
        self.finish_time = finish_time
        self.task_list = []
        
    def __getitem__(self, item):
        return getattr(self, item)

    def addTask(self, task):
        self.task_list.append(task)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
