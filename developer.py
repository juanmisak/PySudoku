from PyQt4.QtGui import QMainWindow
from ui_developer import Ui_Developer
"""Clase que permite mostrar los desarrolladores del juego PySudoku*. 
   :author: Juan Mite
   :version: 1.0"""  
class Developer(QMainWindow):

    def __init__(self):
        """Inicializador de la clase Developer."""  
        QMainWindow.__init__(self)
        self.ui = Ui_Developer()
        self.ui.setupUi(self)    
        self.ui.btnInicio.clicked.connect(self.onBtnInicioClicked)
    
    def setHomeWindow(self, homeWindow):
        """Metodo que obtiene una referencia de la ventana home. 
           :param self: Referencia a la clase. 
           :param value: Referencia a la ventana home""" 
        self.homeWindow = homeWindow
        
    def onBtnInicioClicked(self):
        """Evento regresar a la ventana principal"""
        self.hide()
        self.homeWindow.show()
    

