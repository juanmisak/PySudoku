'''
Created on 24/07/2013

@author:Juan
'''
from PyQt4.QtGui import QMainWindow
from ui_home import Ui_Home
from developer import Developer
from mainwindow import MainWindow
from estadistica import Estadistica

class Home(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Home()
        self.ui.setupUi(self)       
        self.ui.btnJugar    .clicked.connect(self.onBtnJugarClicked)
        self.ui.btnDesarrolladores.clicked.connect(self.onBtnDesarrolladoresClicked)
        self.ui.btnEstadistica.clicked.connect(self.onBtnEstadisticaClicked)

        # Init windows
        self.mainWindow = MainWindow()
        self.mainWindow.setHomeWindow(self)
        self.developersWindow = Developer()
        self.developersWindow.setHomeWindow(self)
        self.highscoresWindow = Estadistica()
        self.highscoresWindow.setHomeWindow(self)
        
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
        self.mainWindow.show()
        self.mainWindow.setDifficulty(difficulty)
        self.mainWindow.newGame(self.ui.txtNombre.text())
            
        # def onBtnDesarrolladoresClicked(self):
        # self.ui.btnDesarrolladores     
    def onBtnDesarrolladoresClicked(self):         
        self.developersWindow.show()
        self.close()
              
    def onBtnEstadisticaClicked(self):
        self.highscoresWindow.show()
        self.setVisible(False)
         
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    
    app = QApplication(sys.argv) 
    h = Home()   
    h.show()

    sys.exit(app.exec_())
