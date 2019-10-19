##> Import default!
import sys

##> Import external!
from PyQt5 import QtWidgets

##> Import own classes!
from Configuration import Configuration
from GUI import GUI

##> Run program!
if __name__ == '__main__':

	##> Setup!
	c = Configuration("./config.json")
	a = QtWidgets.QApplication(sys.argv)
	g = GUI(c.getUiPath())
	
	##> Run!
	g.show()
	a.exec()
	sys.exit() ##> Quit after window is closed!