'''
Created on 25/07/2013

@author:Juan
'''

from PyQt4.QtGui import QMainWindow
from ui_developer import Ui_Developer
#from home import Home

class Developer(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Developer()
        self.ui.setupUi(self)    
        #self.ui.btnInicio.clicked.connect(self.onBtnInicioClicked)
    
    #def onBtnInicioClicked(self):
        #h = Home()
        #h.setVisible(True)
        #self.close()
        