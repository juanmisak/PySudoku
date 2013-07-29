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



class Estadistica(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_Estadistica()
        self.ui.setupUi(self)
        
        self.lienzo=QtGui.QGraphicsScene()
        self.ui.graphicsView.setScene(self.lienzo)

    def setHomeWindow(self, homeWindow):
    	self.homeWindow = homeWindow
        
    def graficarEstadisticas(self,n1,p1,n2,p2,n3,p3,n4,p4,n5,p5):
        self.blackBrush = Qt.QBrush(Qt.QColor("black"))
        self.blackPen = Qt.QPen(Qt.QColor("black"))
        
        self.Puntuacion1 =  200*p1/p1
        self.Puntuacion2 =  200*p2/p1
        self.Puntuacion3 =  200*p3/p1
        self.Puntuacion4 =  200*p4/p1
        self.Puntuacion5 =  200*p5/p1
        self.width = 40
        s=1.5
          
        self.rectangulo = QGraphicsRectItem()
        self.nombre = QGraphicsTextItem()   
        
        self.rectangulo = self.lienzo.addRect(80.0,35.0, self.width,-self.Puntuacion1,self.blackPen,self.blackBrush)
        self.rectangulo = self.lienzo.addRect(160.0,35.0, self.width,-self.Puntuacion2,self.blackPen,self.blackBrush)
        self.rectangulo = self.lienzo.addRect(240.0,35.0, self.width,-self.Puntuacion3,self.blackPen,self.blackBrush)
        self.rectangulo = self.lienzo.addRect(320.0,35.0, self.width,-self.Puntuacion4,self.blackPen,self.blackBrush)
        self.rectangulo = self.lienzo.addRect(400.0,35.0, self.width,-self.Puntuacion5,self.blackPen,self.blackBrush)
        
        self.nombre = self.lienzo.addText(n5)
        self.nombre.setX(385) 
        self.nombre.setY(self.width)
        self.nombre.setScale(s)
        self.nombre = self.lienzo.addText(n4)
        self.nombre.setX(315) 
        self.nombre.setY(self.width) 
        self.nombre.setScale(s)
        self.nombre = self.lienzo.addText(n3)
        self.nombre.setX(225) 
        self.nombre.setY(self.width)
        self.nombre.setScale(s)
        self.nombre = self.lienzo.addText(n2)
        self.nombre.setX(138) 
        self.nombre.setY(self.width)
        self.nombre.setScale(s)
        self.nombre = self.lienzo.addText(n1)
        self.nombre.setX(75) 
        self.nombre.setY(self.width)
        self.nombre.setScale(s)
               
        self.setWindowState(QtCore.Qt.WindowActive)

