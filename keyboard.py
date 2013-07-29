from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QGridLayout, QPushButton





class Keyboard(QWidget):
	
	# Signals
	modeChanged = pyqtSignal(str)
	numberSelected = pyqtSignal(int)

	def __init__(self, parent):
		QWidget.__init__(self, parent)

		self.attachedCell = None
		self.keyboard = QGridLayout()
		self.setLayout(self.keyboard)

		for i in range(1, 10):
			number = QPushButton(str(i))
			number.clicked.connect(self.selectNumber)	
			number.setStyleSheet("color: grey;")			
			# Given a number Z you can deduce a formula to get
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
			# y = 3 - ( z + 2 ) / 3
			
			self.keyboard.addWidget(number, 3-(i+2)/3, (i+2)%3)

		modeButtons = [
			('F', 3, 0, self.setModeToFinal),

			('A', 3, 2, self.setModeToAnnotation)            
      
		]

		for b in modeButtons:
			button = QPushButton(b[0])            
			self.keyboard.addWidget(button, b[1], b[2])
			button.clicked.connect(b[3])                        
		self.hide()

	def selectNumber(self):
		button = self.sender()
		self.hide()
		self.numberSelected.emit( int(button.text()) )

	def setModeToFinal(self):
		self.modeChanged.emit("Final")

	def setModeToAnnotation(self):
		self.modeChanged.emit("Annotation")
	
	def activate(self):
		cell = self.sender()

		if cell != None:

			if self.attachedCell:
				self.numberSelected.disconnect(self.attachedCell.setValue)
				self.modeChanged.disconnect(self.attachedCell.setMode)

			self.numberSelected.connect(cell.setValue)
			self.modeChanged.connect(cell.setMode)
			self.attachedCell = cell
			self.move(cell.pos().x() + 25, cell.pos().y() + 90)
			self.show()

