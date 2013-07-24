from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QMainWindow
from ui_mainwindow import Ui_MainWindow
from cell import Cell
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
		# TODO get difficulty from user input
		self.newGame(2)

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

	def newGame(self, difficulty):
		# Generate new sudoku board
		self.sudoku = Sudoku()
		self.sudoku.cellValueChanged.connect(self.setCellValue)
		self.sudoku.shuffle(difficulty*9 + 3*9)
		self.sudoku.cellValueChanged.disconnect(self.setCellValue)

		# Update the model when the view is changed
		self.cellValueChanged.connect(self.sudoku.setCellValue)

	def setCellValue(self, index, value):
		self.board[index].setValue(value)
		# TODO change color to indicate that it's precalculated

	def setCellValueFromView(self, value):
		c = self.sender()

		self.cellValueChanged.emit( self.board.index(c), value )

if __name__ == '__main__':
	import sys
	from PyQt4.QtGui import QApplication
	
	app = QApplication(sys.argv)

	w = MainWindow()
	w.show()

	sys.exit(app.exec_())
