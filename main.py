import sys
from time import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from Controller.AuthController import AuthController
from Controller.PomController import PomController

class LoginUI(QDialog):
    def __init__(self):
        super(LoginUI, self).__init__()
        loadUi("./UI/login.ui", self)
        
        # This is example of changing screen
        self.loginButton.clicked.connect(self.loginAction)
        self.signUpButton.clicked.connect(self.signupAction)

    def go_main_menu(self, current_user_name):
        main_menu = MainMenuUI()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        main_menu.titleWorkspaceLabel.setText(current_user_name) 

    def loginAction(self):
        global authController
        authController = AuthController()
        resultMsg = authController.login(self.emailInputLogin.text())
        self.errorTextLogin.setText(resultMsg)
        if resultMsg == 'Success':
            self.go_main_menu(authController.current_user.name+"'s Workspace")
    
    def signupAction(self):
        #print(self.emailInputSignUp.text())
        authController = AuthController()
        result_msg = authController.signup(self.emailInputSignUp.text(),self.nameInputSignUp.text())
        self.errorTextSignUp.setText(result_msg)
        
        
class MainMenuUI(QDialog):
    def __init__(self):
        super(MainMenuUI, self).__init__()
        loadUi("./UI/mainMenu.ui", self)
        
        #Initial Load
        self.pomController = PomController(authController.current_user)

        self.deleteRecipientCombo.clear()
        self.deleteRecipientCombo.addItems(self.pomController.getRecipients())
        
        self.projectDeleteCombo.clear()
        self.projectDeleteCombo.addItems(self.pomController.getProjects())
        
        self.selectProjectCombo.clear()
        self.selectProjectCombo.addItems(self.pomController.getProjects())
        
        self.subjectDeleteCombo.clear()
        if self.pomController.getSubjects(self.projectDeleteCombo.currentText()) != None:
            self.subjectDeleteCombo.addItems(self.pomController.getSubjects(self.projectDeleteCombo.currentText()))
        
        self.selectSubjectCombo.clear()
        if self.pomController.getSubjects(self.projectDeleteCombo.currentText()) != None:
            self.selectSubjectCombo.addItems(self.pomController.getSubjects(self.selectProjectCombo.currentText()))
        
        # Event Actions
        self.addRecipientButton.clicked.connect(self.addRecipientAction)
        self.addProjectButton.clicked.connect(self.addProjectAction)
        self.addSubjectButton.clicked.connect(self.addSubjectAction)
        self.deleteRecipientButton.clicked.connect(self.delRecipientAction)
        self.projectDeleteButton.clicked.connect(self.delProjectAction)
        self.projectDeleteCombo.currentTextChanged.connect(self.selectDeleteProjectAction)
        self.selectProjectCombo.currentTextChanged.connect(self.selectProjectAction)
        self.startPomodoroButton.clicked.connect(self.go_pomodoro)

    def go_pomodoro(self):
        pomodoro_ui = PomodoroUI()
        widget.addWidget(pomodoro_ui)
        widget.setCurrentIndex(widget.currentIndex()+1)
        pomodoro_ui.setCurrentSubject(self.selectProjectCombo.currentText(), self.selectSubjectCombo.currentText(),0)
        

    def addRecipientAction(self):
        result_msg = self.pomController.addRecipient(self.addRecipientInput.text())
        if result_msg == "Success":
            self.deleteRecipientCombo.addItem(self.addRecipientInput.text())
            self.addRecipientInput.clear()
        self.errorTextRecipientsEmailLabel.setText(result_msg) 
        
    def delRecipientAction(self):
        self.pomController.delRecipient(self.deleteRecipientCombo.currentText())
        self.deleteRecipientCombo.clear()
        self.deleteRecipientCombo.addItems(self.pomController.getRecipients())
        
    def addProjectAction(self):
        result_msg = self.pomController.addProject(self.addProjectInput.text())
        if result_msg == "Success":
            self.projectDeleteCombo.addItem(self.addProjectInput.text())
            self.selectProjectCombo.addItem(self.addProjectInput.text())
        self.errorTextProjectLabel.setText(result_msg)
        
    def delProjectAction(self):
        self.pomController.delProject(self.projectDeleteCombo.currentText())
        self.projectDeleteCombo.clear()
        self.projectDeleteCombo.addItems(self.pomController.getProjects())
        self.selectProjectCombo.clear()
        self.selectProjectCombo.addItems(self.pomController.getProjects())
        
    def selectDeleteProjectAction(self, p_name):
        self.subjectDeleteCombo.clear()
        if self.pomController.getSubjects(p_name) != None:
            self.subjectDeleteCombo.addItems(self.pomController.getSubjects(p_name))
        
    def selectProjectAction(self, p_name):
        self.selectSubjectCombo.clear()
        if self.pomController.getSubjects(p_name) != None:
            self.selectSubjectCombo.addItems(self.pomController.getSubjects(p_name))

    def addSubjectAction(self):
        result_msg = self.pomController.addSubject(self.selectProjectCombo.currentText(), self.addSubjectInput.text())
        if result_msg == "Success":
            self.subjectDeleteCombo.addItem(self.addSubjectInput.text())
            self.selectSubjectCombo.addItem(self.addSubjectInput.text())
        self.errorTextSubjectLabel.setText(result_msg)


class PomodoroUI(QDialog):
    current_project = ""
    current_subject = ""
    current_session_index = 0
    
    def __init__(self):
        super(PomodoroUI, self).__init__()
        loadUi("./UI/pomodoro.ui", self)
        
        #Initial Load
        self.pomController = PomController(authController.current_user)
        
        # Event Actions
        self.addTask.clicked.connect(self.addTaskAction)


    def setCurrentSubject(self, p_name, s_name, session_index):
        self.current_project = p_name
        self.current_subject = s_name
        self.current_session_index = session_index
        self.pomController.startPomodoro(p_name, s_name)
        self.numberOfSession.setText(session_index)
        
    def addTaskAction(self):
        self.pomController.addTask(self.current_project, self.current_subject,self.current_session_index, self.taskInput.text())
        self.tasksCombo.addItem(self.taskInput.text())
class ShortBreakUI(QDialog):
    def __init__(self):
        super(ShortBreakUI, self).__init__()
        loadUi("./UI/shortBreak.ui", self)


class LongBreakUI(QDialog):
    def __init__(self):
        super(LongBreakUI, self).__init__()
        loadUi("./UI/longBreak.ui", self)


app = QApplication(sys.argv)
UI = LoginUI()  # This line determines which screen you will load at first

# You can also try one of other screens to see them.
# UI = MainMenuUI()
# UI = PomodoroUI()
# UI = ShortBreakUI()
# UI = LongBreakUI()

widget = QtWidgets.QStackedWidget()
widget.addWidget(UI)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.setWindowTitle("Time Tracking App")
widget.show()
sys.exit(app.exec_())
