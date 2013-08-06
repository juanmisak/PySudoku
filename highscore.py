from lamecryptfile import LamecryptFile
import os

class HighScore:

	def __init__(self, userName, seconds, level):
		self.userName = userName
		self.seconds = seconds
		self.level = level

	def __str__(self):
		return str(self.userName) + ':' + str(self.seconds) + ':' + str(self.level)

	def __cmp__(self, other):
		return self.seconds - other.seconds
	
	@staticmethod
	def saveToFile(highscores):
		f = LamecryptFile('highscores', 'w')
		for h in highscores:
			f.write(str(h) + "\n")
		f.close()

	@staticmethod
	def loadFromFile():
		filename = 'highscores'
		if not os.path.isfile(filename):
			open(filename, 'w').close()

		f = LamecryptFile(filename, 'r')
		
		highscores = []

		for strHs in f.read().split("\n"):
			hs = strHs.split(':')	
			if len(hs) == 3:
				highscores.append( HighScore(hs[0], int(hs[1]), hs[2]) )
			
		return highscores

if __name__ == '__main__':
	hs = []
	hs.append( HighScore('user1', 100, 'Easy') )
	hs.append( HighScore('adfasdf', 300, 'Easy') )
	hs.append( HighScore('aaaaa', 20, 'Easy') )
	hs.append( HighScore('blablabl', 9, 'Easy') )
	hs.append( HighScore('wowowowo', 900, 'Hard') )

	hs.sort()
	for h in hs:
		print h

	HighScore.saveToFile(hs)
	hs = HighScore.loadFromFile()

	print '=========================='

	hs.sort()
	for h in hs:
		print h



