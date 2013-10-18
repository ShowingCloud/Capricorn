from PySide import QtCore,QtGui
from UI.ui_setTime import Ui_Dialog
 
#from Translations.tr_rc import *
import sys


class SetDelayTime(QtGui.QDialog):

    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        intVal = QtGui.QIntValidator()
        self.ui.pushButtonStart.setEnabled(False)
        self.ui.lineEditDelayTime.setValidator(intVal)
        self.ui.lineEditDelayTime.textChanged.connect(self.inputChanged)
        self.ui.pushButtonCancel.clicked.connect(self.cancel)
        self.ui.pushButtonStart.clicked.connect(self.start)
    def inputChanged(self):
        if self.ui.lineEditDelayTime.text()=="":
            self.ui.pushButtonStart.setEnabled(False)
        elif int(self.ui.lineEditDelayTime.text())>0:
            self.ui.pushButtonStart.setEnabled(True)
    
    def start(self):
        self.accept()
        
    def cancel(self):
        self.reject()