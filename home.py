from PyQt4.QtGui import QMainWindow
from ui_home import Ui_Home
from developer import Developer
from mainwindow import MainWindow
from estadistica import Estadistica
"""Clase que permite mostar un menu principal al jugador
    donde podra elegir el nivel de juego y ingresar su nombre. 
   :author: Esteban Muñoz
   :version: 1.0"""  
class Home(QMainWindow):

    def __init__(self):
        """Inicializador de la clase Home."""  
        QMainWindow.__init__(self)
        self.ui = Ui_Home()
        self.ui.setupUi(self)  
        """Coneccion de señales."""       
        self.ui.btnJugar    .clicked.connect(self.onBtnJugarClicked)
        self.ui.btnDesarrolladores.clicked.connect(self.onBtnDesarrolladoresClicked)
        self.ui.btnEstadistica.clicked.connect(self.onBtnEstadisticaClicked)

        """Inicializacion de MainWindow.""" 
        self.mainWindow = MainWindow()
        self.mainWindow.setHomeWindow(self)
        self.developersWindow = Developer()
        self.developersWindow.setHomeWindow(self)
        self.highscoresWindow = Estadistica()
        self.highscoresWindow.setHomeWindow(self)
        
    def onBtnJugarClicked(self):
        """Funcion que permite seleccionar un nivel de juego""" 
        """Nivel facil 36 celdas vacias.""" 
        if self.ui.radioButtonFacil.isChecked():
            difficulty = 1
            """Nivel intermedio 36+9 = 45 celdas vacias."""
        elif self.ui.radioButtonIntermedio.isChecked():
            difficulty = 2
            """Nivel dificil 36+9+9 = 63 celdas vacias."""
        elif self.ui.radioButtonDificil.isChecked():
            difficulty = 3
        else:
            difficulty = 1           
        self.setVisible(False)
        self.mainWindow.show()
        self.mainWindow.setDifficulty(difficulty)
        self.mainWindow.newGame(self.ui.txtNombre.text())

    def onBtnDesarrolladoresClicked(self):   
        """Funcion que permite mostrar la ventana de desarrolladores"""        
        self.developersWindow.show()
        self.close()
              
    def onBtnEstadisticaClicked(self):
        """Funcion que permite mostrar la ventana de estadisticas"""     
        self.highscoresWindow.show()
        self.setVisible(False)
