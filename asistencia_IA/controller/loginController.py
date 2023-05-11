import sys
import os
myDir = os.getcwd
sys.path.append(myDir)

from PyQt6 import QtWidgets
from database.ConexionDB import ConexionDB
from model.User import User

class LoginController():
    def __init__(self):
        self.con=ConexionDB()
        self.user = User()
        #self.log_in = log_in
    
    def login(self,user,password):
        print("aqui")
        if(user and password):
            user = self.user.getUser(user,password)

            if(user):
                print(user)
                #self.log_in.hide()
                print("session iniciada")
            
            else:
                print(user)
                print("no existe")
    


