import random
from PyQt4.QtCore import QObject, pyqtSignal

class Sudoku(QObject):

	cellValueChanged = pyqtSignal(int, int)

	def __init__(self):
		QObject.__init__(self)

		self.board = [
			5,3,4,6,7,8,9,1,2,
			6,7,2,1,9,5,3,4,8,
			1,9,8,3,4,2,5,6,7,
			8,5,9,7,6,1,4,2,3,
			4,2,6,8,5,3,7,9,1,
			7,1,3,9,2,4,8,5,6,
			9,6,1,5,3,7,2,8,4,
			2,8,7,4,1,9,6,3,5,
			3,4,5,2,8,6,1,7,9
		]

	@staticmethod
	def fromString(s):
		sudoku = Sudoku()
		sudoku.board = []

		for c in s:
			sudoku.board.append( int(c) )

		return sudoku

	def __str__(self):
		s = ''
		for i in range( len( self.board ) ):
			if ( i % 9 == 0 ): s += "\n"
			s += str( self.board[i] ) + ' '
		return s

	def __repr__(self):
		s = ''
		for c in self.board:
			s += str(c)
		return s

	def setCellValue(self, index, value):
		if self.board[index] != value:
			self.board[index] = value
			self.cellValueChanged.emit(index, value)

	def getCellValue(self, index):
		return self.board[index]

	def shuffle(self, empty):
		''' Swap block rows and columns'''
		for swaps in range(30):
			i = random.randint(0, 2)
			j = random.randint(0, 2)
			k = random.randint(0, 2)
			l = random.randint(0, 2)

			self.__swapBigRow(i, j)
			self.__swapBigColumn(i, j)
			self.__swapRow(k, i, j)
			self.__swapColumn(l, i, j)

		''' Empty cells'''
		while empty > 0:
			i = random.randint(0, 9*9 - 1)

			if self.board[i] != 0:
				self.board[i] = 0
				empty -= 1

		''' Emit signal for filled cells'''
		for i in range( len(self.board) ):
			if self.board[i] != 0:
				self.cellValueChanged.emit(i, self.board[i])

	def __swapBigRow(self, i, j):
		for y in range(3):
			for x in range(9):
				self.__swap(x, y + 3*i, x, y + 3*j)

	def __swapBigColumn(self, i, j):
		for x in range(3):
			for y in range(9):
				self.__swap(x + 3*i, y, x + 3*j, y)

	def __swapRow(self, bigRow, i, j):
		for x in range(9):
			self.__swap(x, 3*bigRow + i, x, 3*bigRow + j)

	def __swapColumn(self, bigColumn, i, j):
		for y in range(9):
			self.__swap(3*bigColumn + i, y, 3*bigColumn + j, y)
	
	def __swap(self, x1, y1, x2, y2):
		a = x1 + y1*9
		b = x2 + y2*9
		self.board[a], self.board[b] = self.board[b], self.board[a]

	def validate(self):
		''' validate columns'''
		for x in range(9):
			
			summation = 0; multiplication = 1
			for y in range(9):
				i = x + 9*y
				summation += self.board[i]
				multiplication *= self.board[i]
				
			if summation != 45 or multiplication != 362880:
				return False

		''' validate rows'''
		for y in range(9):

			summation = 0; multiplication = 1
			for x in range(9):
				i = x + y*9
				summation += self.board[i]
				multiplication *= self.board[i]

			if summation != 45 or multiplication != 362880:
				return False

		''' validate little squares'''
		for i in range(0):
			
			summation = 0; multiplication = 1
			for j in range(9):
				x = ( j % 3 ) + ( (i*3) %  3)
				y = ( j / 3 ) + ( (i/3) %  3)
				k = x + 9*y
				summation += self.board[k]
				multiplication *= self.board[k]

			if summation != 45 or multiplication != 362880:
				return False

		return True
