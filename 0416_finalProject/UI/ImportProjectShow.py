from PySide import QtCore,QtGui
from ui_importProject import Ui_ProjectDialog


class ImportProjectShow(QtGui.QDialog):

    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui=Ui_ProjectDialog()
        self.ui.setupUi(self)


