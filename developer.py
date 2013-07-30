'''
Created on 25/07/2013

@author:Juan
'''

from PyQt4.QtGui import QMainWindow
from ui_developer import Ui_Developer


class Developer(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Developer()
        self.ui.setupUi(self)    
        self.ui.btnInicio.clicked.connect(self.onBtnInicioClicked)
    
    def setHomeWindow(self, homeWindow):
            self.homeWindow = homeWindow
        
    def onBtnInicioClicked(self):
        self.hide()
        self.homeWindow.show()
    

