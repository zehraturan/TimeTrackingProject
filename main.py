import sys
from time import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from Controller.AuthController import AuthController

class LoginUI(QDialog):
    def __init__(self):
        super(LoginUI, self).__init__()
        loadUi("./UI/login.ui", self)

        # This is example of changing screen
        self.loginButton.clicked.connect(self.loginAction)
        self.signUpButton.clicked.connect(self.signupAction)

    def go_main_menu(self):
        main_menu = MainMenuUI()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginAction(self):
        print(self.emailInputLogin.text())
        authController = AuthController()
        resultMsg = authController.login(self.emailInputLogin.text())
        self.errorTextLogin.setText(resultMsg)
        if resultMsg == 'Success':
            self.go_main_menu()
    
    def signupAction(self):
        print(self.emailInputSignUp.text())
        authController = AuthController()
        resultMsg = authController.signup(self.nameInputSignUp.text(),self.emailInputSignUp.text())
        self.errorTextSignUp.setText(resultMsg)
        

class MainMenuUI(QDialog):
    def __init__(self):
        super(MainMenuUI, self).__init__()
        loadUi("./UI/mainMenu.ui", self)


class PomodoroUI(QDialog):
    def __init__(self):
        super(PomodoroUI, self).__init__()
        loadUi("./UI/pomodoro.ui", self)


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
