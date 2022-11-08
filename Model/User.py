import json

from Model.Project import Project
from Model.Subject import Subject
from Model.Pomodoro import Pomodoro
from Model.Task import Task

class User(object):
    def __init__(self, email, name, projects, recipients):
        self.name = name
        self.email = email
        self.projects = projects
        self.recipients = recipients

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def addRecipient(self, r_email):
        if r_email not in self.recipients:
            self.recipients.append(r_email)
            return True
        return False
    
    def delRecipient(self, r_email):
        self.recipients.remove(r_email)
    
    def addProject(self, p_name):
        if p_name not in self.projects:
            proj=Project(p_name,{})
            self.projects.update({p_name:proj})
            return True
        return False
    
    def getProject(self, p_name):
        return self.projects[p_name]
    
    def delProject(self, p_name) :
        del self.projects[p_name]
    
    def addSubject(self, p_name, s_name):
        if s_name not in self.projects[p_name]['subjects']:
            subj = Subject(s_name,[])
            self.projects[p_name]['subjects'][s_name] = subj
            return True
        return False
    
    def getSubjects(self, p_name):
        if p_name in self.projects and type(self.projects[p_name]) == dict:
            return self.projects[p_name]['subjects']
        return None
    
    def newPomodoro(self, p_name, s_name):
        pomodoro = Pomodoro("Pomodoro1")
        self.projects[p_name]['subjects'][s_name]['pomodoro_list'].append(pomodoro) 
        
    def addTask(self, p_name, s_name, session_index, t_name):
        task = Task(t_name, False)
        self.projects[p_name]['subjects'][s_name]['pomodoro_list'][-1]["session_list"][session_index]["task_list"].append(task)
        print(self.projects[p_name]['subjects'][s_name]['pomodoro_list'][-1]["session_list"][session_index])
        return True
        