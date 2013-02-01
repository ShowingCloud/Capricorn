# -*- coding: utf-8 -*-

import sys
from PySide import QtCore,  QtGui
from PySide.QtCore import SIGNAL
from Ui_menu import Ui_MainWindow
from os.path import isfile
import HelpForm
import newImageDlg
import setProperty
import imageWindow
import config
import basicLayout
import test_plot_main3
#import test_plot_main



QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class MainClass(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainClass, self).__init__(parent)
        self.ui = Ui_MainWindow()
        ui = self.ui
        ui.setupUi(self)
        
        ui.action_Save.setEnabled(False)
        self.fileName = None
        self.printer = None
        ui.action_Cut.setEnabled(False) #民人
        ui.action_Copy.setEnabled(False)
        
        image =  QtGui.QImage()
        if image.load("images/icon.png"):
            print 'yes'
            label = QtGui.QLabel().setPixmap(QtGui.QPixmap.fromImage(image))
            self.statusBar().addPermanentWidget(label)
        message = self.tr("状态栏")
        self.statusBar().showMessage(message,  5000)
        
        self.setWindowTitle(self.tr("火秀传媒"))
        self.setMinimumSize(160,160)
        self.resize(980,620)
        
        ui.textEdit.copyAvailable.connect(ui.action_Cut.setEnabled)
        ui.textEdit.copyAvailable.connect(ui.action_Copy.setEnabled)
        
        ui.action_About.triggered.connect(self.about)
        ui.action_Open.triggered.connect(self.openFile)
        ui.action_Save.triggered.connect(self.saveFile)
        ui.action_Save_as.triggered.connect(self.save_asFile)
        ui.action_Copy.triggered.connect(ui.textEdit.copy)
        ui.action_Paste.triggered.connect(ui.textEdit.paste)
        ui.action_Cut.triggered.connect(ui.textEdit.cut)
        ui.action_Documentation.triggered.connect(self.updateDocument)
        ui.action_Exit.triggered.connect(QtGui.qApp.quit)
        ui.action_Properties.triggered.connect(self.setProperty)
        ui.action_Print.triggered.connect(self.filePrint)
        ui.action_Undo.triggered.connect(self.undo)
        ui.action_Redo.triggered.connect(self.redo)
        ui.action_SetLayout.triggered.connect(self.setLayout)
        
        
        ui.action_Image.triggered.connect(self.imageDlg)
        ui.action_ImageWindow.triggered.connect(self.showImageWindow)
        ui.action_Config.triggered.connect(self.configureAndSettings)

        widget = test_plot_main3.Widget(self)
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(widget)
        self.ui.sub_widget.setLayout(mainLayout)
        
        self.connect(ui.textEdit, QtCore.SIGNAL("textChanged()"),ui.action_Save.setEnabled(True))

        ui.action_Save_as.setShortcut(QtGui.QKeySequence.SaveAs)
        ui.action_Save_as.setStatusTip('save as ')
        self.createToolBars()
        self.createDockWindows()

    def setLayout(self):
        dialog = basicLayout.Dialog(self)
        dialog.show()
    
    #right click
    def contextMenuEvent(self, event):
        self.ui.menu_File.exec_(event.globalPos()) 
        
    def configureAndSettings(self):
        con = config.ConfigDialog(self)
        con.exec_()
        
    def imageDlg(self):
        form = newImageDlg.NewImageDlg(self)
        form.show()
        
    def showImageWindow(self):
        print 3
        window = imageWindow.Window(self)
        window.show()
        
    def filePrint(self):
        from PySide.QtGui import QPrinter , QPrintDialog
        if self.printer is None:
            self.printer = QPrinter(QPrinter.HighResolution)
            self.printer.setPageSize(QPrinter.Letter)
        form = QPrintDialog(self.printer, self)
        if form.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.ui.textEdit.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(),
                                size.height())
            painter.drawImage(0, 0, self.ui.textEdit)
            
        
    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.ui.action_Open)
        self.fileToolBar.addAction(self.ui.action_Save)
        self.fileToolBar.addAction(self.ui.action_Save_as)

        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.addAction(self.ui.action_Properties)
        self.editToolBar.addAction(self.ui.action_Print)
        self.editToolBar.addAction(self.ui.action_About)
        
    def setProperty(self):
        form = setProperty.ResizeDlg(64, 128, self)
        form.show()
        if form.exec_():
            width, height = form.result()
            info = '<b>\nwidth = %d and height = %d\n</b>'%(width, height)
            self.ui.textEdit.append(info)
            
    def openFile(self):
        file = QtGui.QFileDialog.getOpenFileName(self)
        self.fileName = file[0]
        if self.fileName:
            self.loadFile()
            self.statusBar().showMessage("File %s loaded"%self.fileName, 3000)
            
    def loadFile(self):
        if isfile (self.fileName):
            ##print self.fileName
            text = open(self.fileName).read()
            self.ui.textEdit.setText(text)
            self.ui.action_Save.setEnabled(False)
            self.setWindowTitle("%s[*] - show_1" % self.fileName)
            ##print text
            

    def saveFile(self):
        ##print 'self.fileName=', self.fileName
        if self.fileName == None:
            file = QtGui.QFileDialog.getSaveFileName (self)
            self.fileName = file[0]
        if isfile(self.fileName):
            file = open(self.fileName, 'w')
            file.write(self.ui.textEdit.toPlainText())
            file.close()
            self.ui.action_Save.setEnabled(False)
            
    def save_asFile(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self)
        filename = fileName[0]
        if filename:
            file = open(filename, 'w')
            file.write(self.ui.textEdit.toPlainText())
            file.close()
    
    def undo(self):
        document = self.ui.textEdit.document()
        document.undo()
    
    def redo(self):
        document = self.ui.textEdit.document()
        document.redo()
        
    def about(self):
        QtGui.QMessageBox.about(self, "About Application",
                "The <b>Application</b> example demonstrates how to write "
                "modern <tt>..GUI applications using Qt.</tt>, with <font color=red>..a menu bar, "
                "toolbars, and a s.</font>tatus bar.")

    def updateDocument(self):
        form = HelpForm.HelpForm("index.html", self)
        form.show()
        
    def createDockWindows(self):
        dock = QtGui.QDockWidget("fire works", self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.customerList = QtGui.QListWidget(dock)
        self.customerList.addItems((
            "John Doe, Harmony Enterprises, 12 Lakeside, Ambleton",
            "Jane Doe, Memorabilia, 23 Watersedge, Beaton",
            "Tammy Shea, Tiblanka, 38 Sea Views, Carlton",
            "Tim Sheen, Caraba Gifts, 48 Ocean Way, Deal",
            "Sol Harvey, Chicos Coffee, 53 New Springs, Eccleston",
            "Sally Hobart, Tiroli Tea, 67 Long River, Fedula"))
        dock.setWidget(self.customerList)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock)
        
        self.ui.menu_File.addAction(dock.toggleViewAction())

        dock = QtGui.QDockWidget("fire goods", self)
        self.paragraphsList = QtGui.QListWidget(dock)
        self.paragraphsList.addItems((
            "Thank you for your payment which we have received today.",
            "Your order has been dispatched and should be with you within "
                "28 days.",
            "We have dispatched those items that were in stock. The rest of "
                "your order will be dispatched once all the remaining items "
                "have arrived at our warehouse. No additional shipping "
                "charges will be made.",
            "You made a small overpayment (less than $5) which we will keep "
                "on account for you, or return at your request.",
            "You made a small underpayment (less than $1), but we have sent "
                "your order anyway. We'll add this underpayment to your next "
                "bill.",
            "Unfortunately you did not send enough money. Please remit an "
                "additional $. Your order will be dispatched as soon as the "
                "complete amount has been received.",
            "You made an overpayment (more than $5). Do you wish to buy more "
                "items, or should we return the excess to you?"))
        dock.setWidget(self.paragraphsList)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock)
        
        self. ui.menu_File.addAction(dock.toggleViewAction())

        self.customerList.currentTextChanged.connect(self.insertCustomer)
        self.paragraphsList.currentTextChanged.connect(self.addParagraph)
        
    def insertCustomer(self, customer):
        if not customer:
            return
        self.ui.textEdit.append('\n<b>%s</b>\n'%customer)


    def addParagraph(self, paragraph):
        if not paragraph:
            return
        self.ui.textEdit.append('\n<font size=6 color=pink>%s</font>\n'%paragraph)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("images/icon.png"))
    myapp = MainClass()
    myapp.show()
    sys.exit(app.exec_())
