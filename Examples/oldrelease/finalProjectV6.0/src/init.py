#coding=utf-8
from PySide import QtGui, QtCore
from Frontend import LoginShow
import sys

def main():
    app = QtGui.QApplication(sys.argv)
    locale = QtCore.QLocale.system().name()
##    appTranslator = QtCore.QTranslator()
##    if appTranslator.load (":/loginWin_" + locale):
##        app.installTranslator (appTranslator)
    window = LoginShow.uiShow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
