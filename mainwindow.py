from PyQt4.QtCore import pyqtSignal,QTimer,QString
from PyQt4.QtGui import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from cell import Cell
from highscore import HighScore

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
		self.ui.actionJUEGO_NUEVO.triggered.connect(self.onActionJuegoNuevoTriggered)
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
			#self.setStyleSheet("font: italic 13pt Courier 50 Pitch; background-color: rgb(82, 163, 53);"#)
			# Change cell value when user change cell value
			c.valueChanged.connect(self.setCellValueFromView)

	def newGame(self,name):
		# Generate new sudoku board
		self.sudoku = Sudoku()
		self.sudoku.cellValueChanged.connect(self.setCellValue)
		self.sudoku.shuffle(self.difficulty*9 + 3*9)
		self.sudoku.cellValueChanged.disconnect(self.setCellValue)		
		# Update the model when the view is changed
		self.cellValueChanged.connect(self.sudoku.setCellValue)
		self.initTimer()
		self.ui.btnJugador.setText(name)

	def endGame(self):
		self.stopTimer()

		userName = str(self.ui.btnJugador.text())
		seconds = int(self.s) + int(self.m) * 60 + int(self.h) * 60 * 60
		difficulty = ['Easy', 'Medium', 'Hard'][self.difficulty - 1]

		# Check if current score is a high scores
		highscores = HighScore.loadFromFile()
		highscores.reverse()
		if seconds < highscores[0].seconds:
			msj = QMessageBox()
			msj.setText( "Puntaje alto" )
			msj.exec_()

			# Put score in highscore
			highscores.append( HighScore(userName, seconds, difficulty) )
			highscores.sort()
			highscores.pop()

			HighScore.saveToFile(highscores)

	def setCellValue(self, index, value):
		
		self.board[index].setValue(value)
		# TODO change color to indicate that it's precalculated

	def setCellValueFromView(self, value):
		c = self.sender()

		self.cellValueChanged.emit( self.board.index(c), value )
	
	def onActionSalirTriggered(self):
		self.close()

	def setHomeWindow(self, homeWindow):
		self.homeWindow = homeWindow

	def setDifficulty(self,value):
		self.difficulty = value
		
	def onActionJuegoNuevoTriggered(self):		
		name = self.ui.btnJugador.text()
		self.newGame(name)
		
		
	def onActionAtrasTriggered(self):		
		self.hide()		
		self.homeWindow.show()
				
	
	def on_endGameButton_triggered(self):
		msj = QMessageBox()

		valid = self.sudoku.validate()

		msj.setText( "Valido" if valid else "No valido" )
		msj.exec_()

		if valid:
			self.endGame()
