from PyQt4.QtCore import pyqtSignal, Qt
from PyQt4.QtGui import QWidget, QGridLayout, QPushButton
"""Clase que permite mostrar un teclado en las celdas
   de la tabla de sudoku en la ventana mainwindow. 
   :author: Ramón Carrillo
   :version: 1.0""" 
class Keyboard(QWidget):
	
	"""Senales requerias en la clase"""	
	modeChanged = pyqtSignal(str)
	numberSelected = pyqtSignal(int)

	def __init__(self, parent):
		"""Inicializador de la clase Keyboard.""" 
		QWidget.__init__(self, parent, Qt.Popup)

		self.attachedCell = None
		self.keyboard = QGridLayout()
		self.setLayout(self.keyboard)
		"""Se generan dinamecamente un teclado con numeros
			del 1 al 9 que permitira setear un numero en el 
			tablero sudoku.""" 

		for i in range(1, 10):
			number = QPushButton(str(i))
			number.clicked.connect(self.selectNumber)	
			number.setStyleSheet("background-color: #0029A3; font:17pt Courier 20 Pitch;color: rgb(255, 255, 255);")
			
			""" #Given a number Z you can deduce a formula to get
					# its row and column. In orden to get the layout
					# y,x| 0 1 2
					# ---|-------
					# 0  | 7 8 9
					# 1  | 4 5 6
					# 2  | 3 2 1
					# 3  |     0
					#
					# one posible formula is
					# x = ( z + 2 ) % 3
					# y = 3 - ( z + 2 ) / 3"""
			
			self.keyboard.addWidget(number, 3-(i+2)/3, (i+2)%3)

		modeButtons = [
			('F', 3, 0, self.setModeToFinal),

			('A', 3, 2, self.setModeToAnnotation)            
      
		]
		"""Permite anadir dos botones adicionales al keyboard que serviran 
			para las anotaciones y final de la misma."""
		for b in modeButtons:
			button = QPushButton(b[0]) 
			self.keyboard.addWidget(button, b[1], b[2])
			button.clicked.connect(b[3])  
			button.setStyleSheet("background-color:#002182; font:17pt Courier Courier 20 Pitch;color: rgb(255, 255, 255);")
			if(button.text()=="F"):
				button.setToolTip("Final")
			if(button.text()=="A"):
				button.setToolTip("Annotation")
			
		self.hide()

	def selectNumber(self):
		"""Obtine el numero que se presiono y emite una senal"""
		button = self.sender()
		self.hide()
		self.numberSelected.emit( int(button.text()) )

	def setModeToFinal(self):
		self.modeChanged.emit("Final")

	def setModeToAnnotation(self):
		self.modeChanged.emit("Annotation")
	
	def activate(self):
		"""Permite saber si se hizo clik en una de las celdas del tablero
		   sudoku y muestra el teclado"""
		cell = self.sender()

		if cell != None:

			if self.attachedCell:
				self.numberSelected.disconnect(self.attachedCell.setValue)
				self.modeChanged.disconnect(self.attachedCell.setMode)

			self.numberSelected.connect(cell.setValue)
			self.modeChanged.connect(cell.setMode)
			self.attachedCell = cell
			x = self.parentWidget().pos().x() + cell.pos().x() + 130
			y = self.parentWidget().pos().y() + cell.pos().y() + 150
			self.move(x, y)
			self.show()

