
from PySide.QtCore import *
from PySide.QtGui import *
import Ui_imageDlg


    
class NewImageDlg(QDialog, Ui_imageDlg.Ui_Dialog):

    def __init__(self, parent=None):
        super(NewImageDlg, self).__init__(parent)
        self.setupUi(self)

        self.color = Qt.red
            
        for value, text in (
                (Qt.SolidPattern, self.tr("Solid")),
                (Qt.Dense1Pattern, self.tr("Dense #1")),
                (Qt.Dense2Pattern, self.tr("Dense #2")),
                (Qt.Dense3Pattern, self.tr("Dense #3")),
                (Qt.Dense4Pattern, self.tr("Dense #4")),
                (Qt.Dense5Pattern, self.tr("Dense #5")),
                (Qt.Dense6Pattern, self.tr("Dense #6")),
                (Qt.Dense7Pattern, self.tr("Dense #7")),
                (Qt.HorPattern, self.tr("Horizontal")),
                (Qt.VerPattern, self.tr("Vertical")),
                (Qt.CrossPattern, self.tr("Cross")),
                (Qt.BDiagPattern, self.tr("Backward Diagonal")),
                (Qt.FDiagPattern, self.tr("Forward Diagonal")),
                (Qt.DiagCrossPattern, self.tr("Diagonal Cross"))):
            self.brushComboBox.addItem(text)  #,  QVariant(value)
            
        self.connect(self.colorButton, SIGNAL("clicked()"),
                     self.getColor)
        self.connect(self.brushComboBox, SIGNAL("activated(int)"),
                     self.setColor)
        self.setColor()
        self.widthSpinBox.setFocus()
        self.setWindowTitle('newImageDlg')

    def getColor(self):
        color = QColorDialog.getColor(Qt.black, self)
        if color.isValid():
            self.color = color
            self.setColor()


    def setColor(self):
        pixmap = self._makePixmap(60, 30)
        self.colorLabel.setPixmap(pixmap)


    def image(self):
        pixmap = self._makePixmap(self.widthSpinBox.value(),
                                  self.heightSpinBox.value())
        return QPixmap.toImage(pixmap)


    def _makePixmap(self, width, height):
        pixmap = QPixmap(width, height)
        style = self.brushComboBox.itemData(
                        self.brushComboBox.currentIndex())
        print ' style=',  style
        ##brush = QBrush(self.color, Qt.BrushStyle(style))
        brush = QBrush(self.color, Qt.SolidPattern)
        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), Qt.white)
        painter.fillRect(pixmap.rect(), brush)
        return pixmap


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = NewImageDlg()
    form.show()
    app.exec_()

