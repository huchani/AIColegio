"""
from view.Loguin import Ui_login
from PyQt6 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec())"""


import sys
from PyQt6.QtWidgets import QWidget,QApplication
from view.Loguin import Ui_login
from controller.loginController import LoginController

class log(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        #eventos
        self.eventos()
        #endEventos
        self.show()
    
    def eventos(self):
        self.ui.btn_Salir.clicked.connect(lambda:self.close())
        self.ui.btn_Login.clicked.connect(self.log)

    def log(self):
        usuario = self.ui.in_User.text()
        password = self.ui.in_Password.text()
        
        l = LoginController()
        l.login(usuario,password)
        """print("ingresados:")
        print(usuario)
        print(password)"""


if __name__ == "__main__":
    print("iniciando la Aplicacion")
    app = QApplication(sys.argv)
    logIn = log()
    sys.exit(app.exec())
