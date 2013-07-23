from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QMainWindow
from ui_mainwindow import Ui_MainWindow
from cell import Cell
from keyboard import Keyboard

class MainWindow(QMainWindow):

	# Signals
	cellValueChanged = pyqtSignal(int, int)

	def __init__(self):
		QMainWindow.__init__(self)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.initBoard()

		#self.cellValueChanged.connect(sudoku.setCellValue)


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


if __name__ == '__main__':
	import sys
	from PyQt4.QtGui import QApplication
	
	app = QApplication(sys.argv)

	w = MainWindow()
	w.show()

	sys.exit(app.exec_())
