from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QGridLayout, QPushButton, QLabel
from keyboard import Keyboard

class Cell(QWidget):

	# Signals
	valueChanged = pyqtSignal(int)
	clicked = pyqtSignal()

	def __init__(self):
		QWidget.__init__(self)

		# Widgets for final mode
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
		# If it's in final mode, set the final value
		if self.mode == 'Final':
			self.value.setText(str(value))
			self.valueChanged.emit(value)
		# if it's in annotation mode, add an annotation
		elif self.mode == 'Annotation':
			self.annotations[self.emptyAnnotation].setText(str(value))
			# Put next annotation on next widget
			self.emptyAnnotation = (self.emptyAnnotation + 1) % 9

	def setMode(self, mode):
		# Show button with final value
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
		self.keyboard = keyboard
		self.clicked.connect(keyboard.activate)

	def mouseReleaseEvent(self, e):
		self.clicked.emit()
