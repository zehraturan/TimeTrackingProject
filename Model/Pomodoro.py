import json

from Model.LongBreak import LongBreak
from Model.Session import Session
from Model.ShortBreak import ShortBreak


class Pomodoro:

    def __init__(self, name, session_list=[], break_list=[], long_break=LongBreak()):
        self.name = name

        self.session_list = [Session('Session1'), Session(
            'Session2'), Session('Session3'), Session('Session4')]
        self.break_list = [ShortBreak("Break1"), ShortBreak(
            "Break2"), ShortBreak("Break3"), ShortBreak("Break4")]
        self.long_break = long_break

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
