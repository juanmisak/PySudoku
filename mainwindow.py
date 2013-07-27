from PyQt4.QtCore import pyqtSignal,QTimer,QString
from PyQt4.QtGui import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from cell import Cell
#from home import Home
from keyboard import Keyboard
from sudoku import Sudoku

class MainWindow(QMainWindow):

	# Signals
	cellValueChanged = pyqtSignal(int, int)

	def __init__(self):
		QMainWindow.__init__(self)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.initBoard()
		self.ui.actionSALIR.triggered.connect(self.onActionSalirTriggered)
		self.ui.actionATRAS.triggered.connect(self.onActionAtrasTriggered)
		
	def initTimer(self):
		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.start()
		self.h = 0
		self.m = 0
		self.s = 0		
		self.timer.timeout.connect(self.timerTimeout)

	def stopTimer(self):
		self.timer.stop()
		
	def timerTimeout(self):
		self.s = self.s + 1
		if self.s > 59:
			self.s = 0
			self.m=self.m + 1
		elif self.m > 59:
			self.m = 0
			self.h= self.h + 1
		elif self.h > 23:
			self.h = 0
		# Write time in a pushButton
		self.ui.btnTiempo.setText(QString ("%1:%2:%3")
                                    .arg (self.h)
                                    .arg (self.m)
                                    .arg (self.s) )
	
	def initBoard(self):
		self.board = []

		self.keyboard = Keyboard(self.ui.centralWidget)

		for i in range(9*9):
			x = i % 9
			y = i / 9
			c = Cell()
			self.board.append(c)
			self.ui.board.addWidget(c, y, x)
			c.setKeyboard(self.keyboard)

			# Change cell value when user change cell value
			c.valueChanged.connect(self.setCellValueFromView)

	def newGame(self, difficulty,name):
		# Generate new sudoku board
		self.sudoku = Sudoku()
		self.sudoku.cellValueChanged.connect(self.setCellValue)
		self.sudoku.shuffle(difficulty*9 + 3*9)
		self.sudoku.cellValueChanged.disconnect(self.setCellValue)		
		# Update the model when the view is changed
		self.cellValueChanged.connect(self.sudoku.setCellValue)
		self.initTimer()
		self.ui.btnJugador.setText(name)

	def endGame(self):
		self.stopTimer()

	def setCellValue(self, index, value):
		self.board[index].setValue(value)
		# TODO change color to indicate that it's precalculated

	def setCellValueFromView(self, value):
		c = self.sender()

		self.cellValueChanged.emit( self.board.index(c), value )
	
	def onActionSalirTriggered(self):
		self.close()
	
	def setHome(self,v):
		self.atras = v
		
	
	def onActionAtrasTriggered(self):		
		self.hide()
		self.atras.show()
				
	
	def on_endGameButton_triggered(self):
		msj = QMessageBox()

		valid = self.sudoku.validate()

		msj.setText( "Valido" if valid else "No valido" )
		msj.exec_()

		if valid:
			self.endGame()
