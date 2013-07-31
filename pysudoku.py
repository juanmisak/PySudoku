import subprocess 
import os
import sys


uis = ['developer', 'estadistica', 'home', 'loadgames', 'mainwindow']

for ui_name in uis:
	# Test if generated .py file exists
	if not os.path.isfile('ui_' + ui_name + '.py'):

		# Generate .py from .ui files
		fin = ui_name + '.ui'
		fout = 'ui_' + ui_name + '.py'
		r = subprocess.call('pyuic4 -o ' + fout + ' ' + fin, shell=True) 
		
		if r != 0:
			print 'Error generating ' + fout
			sys.exit(1)

from home import Home
from PyQt4.QtGui import QApplication

app = QApplication(sys.argv) 
h = Home()   
h.show()

sys.exit(app.exec_())
