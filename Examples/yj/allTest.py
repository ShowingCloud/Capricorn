#!/usr/bin/python
#_*_encoding:utf-8_*_
#allTest.py


import sys
from PySide import QtGui, QtCore

class AllTest(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)

##        self.setGeometry(300, 300, 250, 150)
        self.resize(600, 400)
        self.setWindowTitle("All Test")
        icon = QtGui.QIcon()
        #自己添加图片做标题
        icon.addPixmap(QtGui.QPixmap("I:\pythonWork\project\images\preview1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        #创建行动,第一个是图标，第二个是名称
        exit = QtGui.QAction('Exit', self)
        exitIcon = QtGui.QIcon()
        exitIcon.addPixmap(QtGui.QPixmap("I:\pythonWork\project\images\delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        exit.setIcon(exitIcon)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')   

        
        #菜单栏
        menuBar = self.menuBar()
        file = menuBar.addMenu('&File')
        file.addAction(exit)

        #工具栏
        toolBar = self.addToolBar('&Exit')
        toolBar.addAction(exit)

        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        
        #提示工具
        self.setToolTip('This is a new avatar')
        #设置字体
        QtGui.QToolTip.setFont(QtGui.QFont('oldEnglish', 10))
        
        
        #按钮处理事件
        self.quit = QtGui.QPushButton('Clear', self)
        self.quit.setGeometry(80, 100, 60, 25)
        #按钮触发事件，关闭程序
        self.quit.connect(QtCore.SIGNAL('clicked()'), self.clearContent)

        
        #界面在整个窗口的正中间
        self.center()
        
        #添加文本框
        self.textEdit = QtGui.QTextEdit('Hello world!', self)
        self.textEdit.setGeometry(150,100, 250, 150)

        #设置颜色
        self.color = QtGui.QColor(0, 0, 0)
        self.textEdit.setStyleSheet("QWidget{background-color: %s}" % self.color.name())
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('cleanlooks'))
        
        #把文本编辑框添加到中间
##        self.setCentralWidget(self.textEdit)

        #标签和输入文本框,button
        self.nameTabel = QtGui.QLabel("Name:", self)
        self.nameTabel.setGeometry(150, 70, 30, 25)
        self.pwdTabel = QtGui.QLabel("PWD:", self)
        self.pwdTabel.setGeometry(250, 70, 25, 25)
        self.nameEdit = QtGui.QLineEdit(self)
        self.nameEdit.setGeometry(185, 70, 60, 25)
        self.pwdEdit = QtGui.QLineEdit(self)
        self.pwdEdit.setGeometry(280, 70, 60, 25)
        self.goButton = QtGui.QPushButton("Go", self)
        self.goButton.setGeometry(360, 70, 40, 25)

        self.goButton.connect(QtCore.SIGNAL('clicked()'), self.showInfo)

        #打开文件对话框
        self.open = QtGui.QPushButton('Open', self)
        self.open.setGeometry(80, 135, 60, 25)
        self.open.connect(QtCore.SIGNAL('clicked()'), self.openFile)

        #保存文件对话框(另存为)
        self.save = QtGui.QPushButton('Save', self)
        self.save.setGeometry(80, 170, 60, 25)
        self.save.connect(QtCore.SIGNAL('clicked()'), self.saveFile)


        #红色按钮
        self.red = QtGui.QPushButton('Red', self)
        self.red.setGeometry(420, 135, 60, 25)
        self.red.connect(QtCore.SIGNAL('clicked()'), self.changeRed)

        #绿色按钮
        self.green = QtGui.QPushButton('Green', self)
        self.green.setGeometry(420, 170, 60, 25)
        self.green.connect(QtCore.SIGNAL('clicked()'), self.changeGreen)

        #蓝色按钮
        self.blue = QtGui.QPushButton('Blue', self)
        self.blue.setGeometry(420, 100, 60, 25)
        self.blue.connect(QtCore.SIGNAL('clicked()'), self.changeBlue)

        

        #状态栏
        #showMessage()方法显示信息
        self.statusBar().showMessage('Test')


        #创建右键菜单
        self.createContextMenu()
        


    def closeEvent(self, event):
        #关闭触发弹出确认框按钮(有两个按钮的提示框)
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()

        else:
            #忽略事件
            event.ignore()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()

        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2 )
        


    def createContextMenu(self):
        """
        创建右键菜单
        必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        否则无法使用customContextMenuRequested信号
        """
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        self.contextMenu = QtGui.QMenu(self)
        self.actionA = self.contextMenu.addAction('ActionA')
        self.actionB = self.contextMenu.addAction('ActionB')
        self.actionC = self.contextMenu.addAction('ActionC')

        # 将动作与处理函数相关联  
        # 这里为了简单，将所有action与同一个处理函数相关联，  
        # 当然也可以将他们分别与不同函数关联，实现不同的功能

        self.actionA.triggered.connect(self.actionHandler)
        self.actionB.triggered.connect(self.actionHandler)
        self.actionC.triggered.connect(self.actionHandler)

    def showContextMenu(self, pos):
        ''' 
        右键点击时调用的函数 
        '''  
        # 菜单显示前，将它移动到鼠标点击的位置

        self.contextMenu.move(self.pos() + pos)
        self.contextMenu.show()


    def actionHandler(self):
        '''
        菜单中的具体action调用函数
        '''
        self.textEdit.setText("Context menu action!")
        
    def clearContent(self):
        self.textEdit.setText("")
        self.nameEdit.setText('')
        self.pwdEdit.setText('')

        
    def showInfo(self):
        if self.nameEdit.text() == "" or self.pwdEdit.text() == "":
            self.textEdit.setText("Please input your account and password login the system!")
        else:
            self.textEdit.setText("Name:"+self.nameEdit.text() + "\tPWD:" +self.pwdEdit.text())


    def openFile(self):
        #fileName相当于一个元组，第一个才是要打开文件的绝对路径
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.')
        file = open(fileName[0])
        data = file.read()
        self.textEdit.setText(data)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.textEdit.setText("Welcome in my system!")
            self.nameEdit.setText('')
            self.pwdEdit.setText('')

    #另存为实现函数
    def saveFile(self):
        fd = QtGui.QFileDialog()
        self.fileName = fd.getSaveFileName(self, 'Save file', '.')
        fobj = open(self.fileName[0], 'w')
        fobj.write(self.textEdit.toPlainText())
        fobj.close()
        self.textEdit.setText("File saved!")

    def changeRed(self):
        if self.red.isChecked():
            self.color.setRed(255)
        else:
            self.color.setRed(0)

        self.textEdit.setStyleSheet("QWidget{background-color: %s}" % self.color.name())


    def changeGreen(self):
        if self.red.isChecked():
            self.color.setGreen(255)
        else:
            self.color.setGreen(0)

        self.textEdit.setStyleSheet("QWidget{background-color: %s}" % self.color.name())


    def changeBlue(self):
        if self.red.isChecked():
            self.color.setBlue(255)
        else:
            self.color.setBlue(0)

        self.textEdit.setStyleSheet("QWidget{background-color: %s}" % self.color.name())

    
app = QtGui.QApplication(sys.argv)
test = AllTest()
test.show()
sys.exit(app.exec_())
