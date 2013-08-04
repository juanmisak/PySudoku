'''
Created on 25/07/2013

/**
 * La clase Estadistica representa un Widget para los jugadores.
 * @author Juan Mite
 */
'''

from PyQt4.QtGui import QGraphicsRectItem,QGraphicsTextItem
from ui_estadistica import Ui_Estadistica
from PyQt4 import QtCore,QtGui,Qt
from highscore import HighScore



class Estadistica(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_Estadistica()
        self.ui.setupUi(self)
        self.ui.pushButton_7.clicked.connect(self.onBtnInicioClicked)
        
        self.lienzo=QtGui.QGraphicsScene()
        self.ui.graphicsView.setScene(self.lienzo)

        self.graficar( HighScore.loadFromFile() )

    def setHomeWindow(self, homeWindow):
        self.homeWindow = homeWindow

    def graficar(self, hs):
        self.graficarEstadisticas(hs[0].userName, hs[0].seconds,
                hs[1].userName, hs[1].seconds,
                hs[2].userName, hs[2].seconds,
                hs[3].userName, hs[3].seconds,
                hs[4].userName, hs[4].seconds)

    def graficarEstadisticas(self,n1,p1,n2,p2,n3,p3,n4,p4,n5,p5):
        self.blackBrush = Qt.QBrush(Qt.QColor("black"))
        self.blackPen = Qt.QPen(Qt.QColor("black"))
        
                
        self.Puntuacion1 = 200-(180*p1/p5)
        self.Puntuacion2 = 200-(180*p2/p5)
        self.Puntuacion3 = 200-(180*p3/p5)
        self.Puntuacion4 = 200-(180*p4/p5)
        self.Puntuacion5 = 200-(180*p5/p5)
        self.width = 40
        self.widthN = 80
        s=1.5
          
        self.rectangulo = QGraphicsRectItem()
        self.nombre = QGraphicsTextItem()   
        
        self.rectangulo = self.lienzo.addRect(-180.0,self.widthN, self.width,-self.Puntuacion1,self.blackPen,self.blackBrush)
        self.rectangulo = self.lienzo.addRect(-100.0,self.widthN, self.width,-self.Puntuacion2,self.blackPen,self.blackBrush)
        self.rectangulo = self.lienzo.addRect(-20.0,self.widthN, self.width,-self.Puntuacion3,self.blackPen,self.blackBrush)
        self.rectangulo = self.lienzo.addRect(40.0,self.widthN, self.width,-self.Puntuacion4,self.blackPen,self.blackBrush)
        self.rectangulo = self.lienzo.addRect(120.0,self.widthN, self.width,-self.Puntuacion5,self.blackPen,self.blackBrush)
        
        self.nombre = self.lienzo.addText(n5)
        self.nombre.setX(120) 
        self.nombre.setY(self.widthN)
        self.nombre.setScale(s)
        self.nombre = self.lienzo.addText(n4)
        self.nombre.setX(40) 
        self.nombre.setY(self.widthN) 
        self.nombre.setScale(s)
        self.nombre = self.lienzo.addText(n3)
        self.nombre.setX(-40) 
        self.nombre.setY(self.widthN)
        self.nombre.setScale(s)
        self.nombre = self.lienzo.addText(n2)
        self.nombre.setX(-130) 
        self.nombre.setY(self.widthN)
        self.nombre.setScale(s)
        self.nombre = self.lienzo.addText(n1)
        self.nombre.setX(-200) 
        self.nombre.setY(self.widthN)
        self.nombre.setScale(s)
               
        
        
    def onBtnInicioClicked(self):
        self.hide()
        self.homeWindow.show()
        
        self.setWindowState(QtCore.Qt.WindowActive)
