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
        self.ui.btnJugar.clicked.connect(self.onBtnJugarClicked)
        self.ui.btnDesarrolladores.clicked.connect(self.onBtnDesarrolladoresClicked)
        self.ui.btnEstadistica.clicked.connect(self.onBtnEstadisticaClicked)
        
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
        self.w.setHome(self)
        self.w.show()           
        self.w.newGame(difficulty,self.ui.txtNombre.text())
            
        # def onBtnDesarrolladoresClicked(self):
        # self.ui.btnDesarrolladores 
    def onBtnDesarrolladoresClicked(self): 
        self.d = Developer()
        self.d.setVisible(True)
        self.close()
              
    def onBtnEstadisticaClicked(self):
        self.e = Estadistica()
        self.e.setVisible(True)
        self.e.graficarEstadisticas("Juan",130,"Esteban",106,"Ramon",84,"Micka",50,"Andrea",40)
        self.close()
    
    
          
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    
    app = QApplication(sys.argv) 
    h = Home()   
    h.show()

    sys.exit(app.exec_())
