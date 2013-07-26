'''
Created on 25/07/2013

/**
 * La clase Estadistica representa un Widget para los jugadores.
 * @author Juan Mite
 */
'''
from PyQt4.QtGui import QMainWindow,QBrush,QPen,QColor,QGraphicsRectItem,QGraphicsScene,QGraphicsTextItem
from ui_estadistica import Ui_Estadistica
from PyQt4.QtCore import Qt
class Estadistica(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Estadistica()
        self.lienzo = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.lienzo)
        self.lienzo.setBackgroundBrush(QColor(82,163,53,255))
        self.ui.setupUi(self)  
        
    def graficarEstadisticas(self,n1,p1,n2,p2,n3,p3,n4,p4,n5,p5):
        self.Puntuacion1 =  200*p1/p1
        self.Puntuacion2 =  200*p2/p1
        self.Puntuacion3 =  200*p3/p1
        self.Puntuacion4 =  200*p4/p1
        self.Puntuacion5 =  200*p5/p1
        self.width = 40
        self.blackBrush = QBrush(Qt.black)
        self.blackPen = QPen(Qt.black)          
        self.rectangulo = QGraphicsRectItem()
        self.nombre = QGraphicsTextItem()   
        
        self.rectangulo = self.lienzo.addRect(80.0,35.0, self.width,-p1,self.blackPen,self.blackBrush)
        self.nombre = self.lienzo.addText(n1)  
        self.nombre.setX(80) 
        self.nombre.setX(40)
        
        self.rectangulo = self.lienzo.addRect(160.0,35.0, self.width,-p2,self.blackPen,self.blackBrush)
        self.nombre = self.lienzo.addText(n2)
        self.nombre.setX(160) 
        self.nombre.setX(40)
                                          
        self.rectangulo = self.lienzo.addRect(240.0,35.0, self.width,-p3,self.blackPen,self.blackBrush)
        self.nombre = self.lienzo.addText(n3)
        self.nombre.setX(240) 
        self.nombre.setX(40)
        
        self.rectangulo = self.lienzo.addRect(320.0,35.0, self.width,-p4,self.blackPen,self.blackBrush)
        self.nombre = self.lienzo.addText(n4) 
        self.nombre.setX(320) 
        self.nombre.setX(40)
        
        self.rectangulo = self.lienzo.addRect(400.0,35.0, self.width,-p5,self.blackPen,self.blackBrush)
        self.nombre = self.lienzo.addText(n5) 
        self.nombre.setX(400)  
        self.nombre.setX(40)