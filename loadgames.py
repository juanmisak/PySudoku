from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QDialog, QStandardItemModel, QStandardItem
from ui_loadgames import Ui_loadGames
from datetime import date
from lamecryptfile import LamecryptFile
from sudoku import Sudoku
import os

class Game:

	def __init__(self, userName, seconds, board):
		self.userName = userName
		self.seconds = seconds
		self.board = board
	
	def __str__(self):
		return self.userName + "\t\t" + \
		       str(self.seconds)

	def __repr__(self):
		return self.userName + ':' + \
		       str(self.seconds) + ':' + \
		       repr(self.board)

	@staticmethod
	def saveToFile(games):
		f = LamecryptFile('savedgames', 'w')
		
		for g in games:
			f.write(repr(g) + "\n")
			f.close
	
	@staticmethod
	def loadFromFile():
		filename = 'savedgames'
		if not os.path.isfile(filename):
			open(filename, 'w').close()

		f = LamecryptFile(filename, 'r')

		games = []

		for strG in f.read().split("\n"):
			g = strG.split(':')
			if len(g) == 3:
				games.append( Game(g[0], int(g[1]), Sudoku.fromString(g[2])) )

		return games


class LoadGames(QDialog):
	
	def __init__(self, parent):
		QDialog.__init__(self, parent)

		self.ui = Ui_loadGames()
		self.ui.setupUi(self)
		self.loadData()
	
	def loadData(self):
		model = QStandardItemModel()

		self.games = Game.loadFromFile()
		
		items = []
		for g in self.games:
			items.append(str(g))
			
		for i in items:
			model.appendRow( QStandardItem(i) ) 
		
		self.ui.listView.setModel(model)

	def on_pushButton_3_clicked(self):
		self.close()

	def on_pushButton_clicked(self):
		sel = self.ui.listView.selectedIndexes()
		if len(sel) == 1:
			g = self.games[ sel[0].row() ]
			self.parent().newGame(g.userName, g.seconds, g.board)
			self.close()

if __name__ == '__main__':
	import sys
	from PyQt4.QtGui import QApplication

	app = QApplication(sys.argv) 
	h = LoadGames()
	h.show()

	sys.exit(app.exec_())
