from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QGridLayout, QPushButton, QLabel
from keyboard import Keyboard
"""Clase que permite agragar celdas a mi layout*. 
   :author: Ramon Carrillo & Esteban Munoz
   :version: 1.0"""  
class Cell(QWidget):

	"""Senales requerias en la clase"""	
	valueChanged = pyqtSignal(int)
	clicked = pyqtSignal()

	def __init__(self):
		"""Inicializador de la clase Cell."""
		QWidget.__init__(self)
		"""Widgets para el modelo final"""
		self.value = QPushButton()
		self.value.clicked.connect(self.clicked)

		# Widgets for annotation mode
		self.annotations = []
		for i in range(9):
			self.annotations.append( QLabel('--') )
		# Put first annotation on first widget
		self.emptyAnnotation = 0

		# Layout
		self.layout = QGridLayout()
		self.setLayout(self.layout)

		self.setMode('Final')

	def setValue(self, value):
		"""Si es un modelo final,se anade un valor final. 
    	   :param self: Referencia a la clase. 
           :param value: Valor a seterar""" 
		# If it's in final mode, set the final value
		if self.mode == 'Final':
			self.value.setText(str(value))
			self.valueChanged.emit(value)
			if (value == 0):
				self.setStyleSheet("font: italic 26pt Courier 20 Pitch; background-color: rgb(82, 163, 53);border-image: url(:/images/Mysitemyway-Blue-Jeans-Social-Media-Delicious-square.ico);")
				self.value.setText("")
			else:
				self.setStyleSheet("font:26pt Courier 20 Pitch; background-color: rgb(82, 163, 53);")
		# if it's in annotation mode, add an annotation
		elif self.mode == 'Annotation':
			self.annotations[self.emptyAnnotation].setText(str(value))
			self.setStyleSheet("font: italic 10pt Courier 29 Pitch; background-color: rgb(82, 163, 53);")
			# Put next annotation on next widget
			self.emptyAnnotation = (self.emptyAnnotation + 1) % 9

	def setMode(self, mode):
		"""Muestra el boton con el valor final. 
    	   :param self: Referencia a la clase. 
           :param mode: modo que se seterar""" 
		'''Show button with final value'''
		if mode == 'Final':
			for a in self.annotations:
				a.hide()
			self.value.show()
			self.layout.addWidget(self.value)
		# Show annotations
		elif mode == 'Annotation':
			self.value.hide()
			for i in range(9):
				self.annotations[i].show()
				self.layout.addWidget(self.annotations[i], i/3, i%3)
		
		self.mode = mode

	def setKeyboard(self, keyboard):
		"""Anade el keyboard a la celda. 
    	   :param self: Referencia a la clase. 
           :param keyboard: teclado """ 
		self.keyboard = keyboard
		self.clicked.connect(keyboard.activate)

	def mouseReleaseEvent(self, e):
		"""Evento que permite emitir una senal al keyboard"""
		self.clicked.emit()
