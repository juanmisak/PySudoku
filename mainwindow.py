from PyQt4.QtCore import pyqtSignal,QTimer,QString
from PyQt4.QtGui import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from cell import Cell
from highscore import HighScore
from loadgames import Game, LoadGames

from keyboard import Keyboard
from sudoku import Sudoku
"""Clase que permite agragar celdas a mi layout*. 
   :author: Esteban Munoz & Ramon Carrillo 
   :version: 1.0""" 
class MainWindow(QMainWindow):

    # Signals
    cellValueChanged = pyqtSignal(int, int)

    def __init__(self):
        QMainWindow.__init__(self)
        """Inicializador de la clase MainWindow."""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """Inicializacion del tablero.""" 
        self.initBoard()
        """Coneccion de senales.""" 
        self.ui.actionJUEGO_NUEVO.triggered.connect(self.onActionJuegoNuevoTriggered)
        self.ui.actionSALIR.triggered.connect(self.onActionSalirTriggered)
        self.ui.actionATRAS.triggered.connect(self.onActionAtrasTriggered)

        self.loadGamesWindow = LoadGames(self)

    def initTimer(self, elapsedSeconds):
        """Funcion que permite inicializar el timer
           que se utilizara al inicio del juego.""" 
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.h = elapsedSeconds / 3600
        self.m = (elapsedSeconds - 3600*self.h) / 60
        self.s = (elapsedSeconds - 3600*self.h) % 60
        """Coneccion de senales."""  
        self.timer.timeout.connect(self.timerTimeout)

    def stopTimer(self):
        """Detiene el timer.""" 
        self.timer.stop()
        
    def timerTimeout(self):
        """Funcion que permite tener actualizado el 
           timer mientras el jugador tenga activo el juego.""" 
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
        """Funcion que permite inicializar el tablero 
           con 81 celdas que el jugador tendra le quellar
           segun el nuevel de dificultad seleccionado al inicio del juego""" 
        self.board = []

        self.keyboard = Keyboard(self)

        for i in range(9*9):
            x = i % 9
            y = i / 9
            c = Cell()
            
            self.board.append(c)
            self.ui.board.addWidget(c, y, x)
            
            c.setKeyboard(self.keyboard) 
            c.valueChanged.connect(self.setCellValueFromView)

    def newGame(self, name, elapsedSeconds = 0, sudoku = None):
        """Se genera un nuevo juego de sudoku con el nombre del jugador y el nivel."""  
        if sudoku == None:
            self.sudoku = Sudoku()
            self.sudoku.shuffle(self.difficulty*9 + 3*9)
        else:
            self.sudoku = sudoku
        self.sudoku.cellValueChanged.connect(self.setCellValue)
        self.sudoku.triggerChanges()
        self.sudoku.cellValueChanged.disconnect(self.setCellValue)
        """Actualiza el modelo cuando la vista es cambiada."""    
        self.cellValueChanged.connect(self.sudoku.setCellValue)
        self.initTimer(elapsedSeconds)
        self.ui.btnJugador.setText(name)

    def endGame(self):   
        """Finaliza el juego."""       
        self.stopTimer()

        userName = str(self.ui.btnJugador.text())
        seconds = int(self.s) + int(self.m) * 60 + int(self.h) * 60 * 60
        difficulty = ['Easy', 'Medium', 'Hard'][self.difficulty - 1]

        ''' Check if current score is a high scores'''
        highscores = HighScore.loadFromFile()
        highscores.reverse()
        if seconds < highscores[0].seconds:
            msj = QMessageBox()
            msj.setText( "Puntaje alto" )
            msj.exec_()

            '''Put score in highscore'''
            highscores.append( HighScore(userName, seconds, difficulty) )
            highscores.sort()
            highscores.pop()

            HighScore.saveToFile(highscores)

    def setCellValue(self, index, value):
        
        self.board[index].setValue(value)
        '''TODO change color to indicate that it's precalculated'''

    def setCellValueFromView(self, value):
        c = self.sender()

        self.cellValueChanged.emit( self.board.index(c), value )
    
    def onActionSalirTriggered(self):
        self.close()

    def setHomeWindow(self, homeWindow):
        """Metodo que obtiene una referencia de la ventana home. 
           :param self: Referencia a la clase. 
           :param value: Referencia a la ventana home""" 
        self.homeWindow = homeWindow

    def setDifficulty(self,value):
        """Se agrega la dificultad a la clase."""
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

    def on_actionGUARDAR_triggered(self):
        userName = str(self.ui.btnJugador.text())
        seconds = int(self.s) + int(self.m) * 60 + int(self.h) * 60 * 60

        games = Game.loadFromFile()
        games.append( Game(userName, seconds, self.sudoku) )
        Game.saveToFile(games)

    def on_actionCARGAR_triggered(self):
        self.loadGamesWindow.loadData()
        self.loadGamesWindow.show()

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

		self.loadGamesWindow = LoadGames(self)

	def initTimer(self, elapsedSeconds):
		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.start()
		self.h = elapsedSeconds / 3600
		self.m = (elapsedSeconds - 3600*self.h) / 60
		self.s = (elapsedSeconds - 3600*self.h) % 60
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

		self.keyboard = Keyboard(self)

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

	def newGame(self, name, elapsedSeconds = 0, sudoku = None):
		if sudoku == None:
			# Generate new sudoku board
			self.sudoku = Sudoku()
			self.sudoku.shuffle(self.difficulty*9 + 3*9)
		else:
			self.sudoku = sudoku

		self.sudoku.cellValueChanged.connect(self.setCellValue)
		self.sudoku.triggerChanges()
		self.sudoku.cellValueChanged.disconnect(self.setCellValue)		
		# Update the model when the view is changed
		self.cellValueChanged.connect(self.sudoku.setCellValue)
		self.initTimer(elapsedSeconds)
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

	def on_actionGUARDAR_triggered(self):
		userName = str(self.ui.btnJugador.text())
		seconds = int(self.s) + int(self.m) * 60 + int(self.h) * 60 * 60

		games = Game.loadFromFile()
		games.append( Game(userName, seconds, self.sudoku) )
		Game.saveToFile(games)

	def on_actionCARGAR_triggered(self):
		self.loadGamesWindow.loadData()
		self.loadGamesWindow.show()
