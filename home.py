'''
Created on 24/07/2013

@author: Esteban
'''

from PyQt4.QtGui import QMainWindow,QMessageBox
from ui_home import Ui_Home
#from developer import Developer
from mainwindow import MainWindow
class Home(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
       # self.timer.timeout.connect(self.timerTimeout)
        self.ui.btnJugar.clicked.connect(self.onBtnJugarClicked)
    
    def onBtnJugarClicked(self):
        # Facil 36 vacias
        if self.ui.radioButtonFacil.isChecked():
            difficulty = 1
        # Intermedio 36+9 = 45vacias
        elif self.ui.radioButtonIntermedio.isChecked():
            difficulty = 2
        # Dificil 36+9+9 = 63vacias
        elif self.ui.radioButtonDificil.isChecked():
            difficulty = 3
        else:
            difficulty = 1           
        self.setVisible(False)
        self.w = MainWindow()
        self.w.show()
        self.w.newGame(difficulty)
            
    #def onBtnDesarrolladoresClicked(self):
       # self.ui.btnDesarrolladores
            
            
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    
    app = QApplication(sys.argv)

    h = Home()
    h.show()

    sys.exit(app.exec_())
