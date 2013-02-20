#coding=utf-8
'''
Created on 2013-2-19

@author: pyroshow
'''
import sys, rc_picture
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *



def createConnection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("my.db")
    db.open()
    
class OperationDatabase():
    
    def __init__(self):
        self.q = QSqlQuery() 
        self.q.exec_(u"create table if not exists Fireworks(id integer primary key autoincrement, FireworkID varchar(20) not null, IgnitorID  varchar(20) not null, ConnectorID varchar(20) not null, Duration integer not null, Inventory integer not null, Color integer not null, Angle integer not null)")
        self.q.exec_("commit")
            
    def insertData(self, *value):
        self.q.prepare("insert into Fireworks(FireworkID, IgnitorID, ConnectorID, Duration, Inventory, Color, Angle) values(?, ?, ?, ?, ?, ?, ?)")
        self.q.bindValue(0, value[0])
        self.q.bindValue(1, value[1])
        self.q.bindValue(2, value[2])
        self.q.bindValue(3, value[3])
        self.q.bindValue(4, value[4])
        self.q.bindValue(5, value[5])
        self.q.bindValue(6, value[6])
        self.q.exec_()
        self.q.exec_("commit")



class StockDiaog(QDialog):
    
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        
        self.setWindowTitle(u"综合显示")
        self.setWindowIcon(QIcon(":/images/title.png"))
        #设置分离器为水平方向
        mainSplitter = QSplitter(Qt.Horizontal)
        #设置分离器为不透明的
        mainSplitter.setOpaqueResize(True)
        
        self.listWidget = QListWidget(mainSplitter)
        self.listWidget.insertItem(0, u"烟花资料")
        self.listWidget.insertItem(1, u"加入组合")
        self.listWidget.insertItem(2, u"编辑脚本")
        
        frame = QFrame(mainSplitter)
        self.stack = QStackedWidget()
        #设置栈窗口的格式为内嵌凸起的
        self.stack.setFrameStyle(QFrame.Panel | QFrame.Raised)
        
        fireworkInfo = FireworkInfo()
        combination = Combination()
        script = Script()
        self.stack.addWidget(fireworkInfo)
        self.stack.addWidget(combination)
        self.stack.addWidget(script)
        
        amendBtn = QPushButton(u"导出")
        closeBtn = QPushButton(u"关闭")
        
        btnLayout = QHBoxLayout()
        #可伸缩的
        btnLayout.addStretch(1)
        btnLayout.addWidget(amendBtn)
        btnLayout.addWidget(closeBtn)
        
        mainLayout = QVBoxLayout(frame)
#        mainLayout.setMargin(10)
        mainLayout.setSpacing(6)
        mainLayout.addWidget(self.stack)
        mainLayout.addLayout(btnLayout)
        
        self.connect(self.listWidget, SIGNAL("currentRowChanged(int)"), self.stack, SLOT("setCurrentIndex(int)"))
        self.connect(closeBtn, SIGNAL("clicked()"), self, SLOT("close()"))
        
        layout = QHBoxLayout()
        layout.addWidget(mainSplitter)
        self.setLayout(layout)
        
        
        self.faderWidget = None
        self.connect(self.listWidget, SIGNAL("currentItemChanged(QListWidgetItem, QListWidgetItem)"), self.changePage)
        self.connect(self.stack, SIGNAL("currentChanged(int)"), self.fadeInWidget)
        
        self.resize(900, 400)
        
        
    def changePage(self, current,previous):
        if not current:
            current = previous
            
        self.stack.setCurrentWidget(current)
    
    def fadeInWidget(self, index):
        
        self.faderWidget = FaderWidget(self.stack.widget(index))
        self.faderWidget.start()
        
        
class FaderWidget(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        if parent:
            self.startColor=parent.palette().window().color()  
        else:
            self.startColor = Qt.white
            
        self.currentAlpha = 0
        self.duration = 1000
        
        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL("timeout()"), self.update)
        #设置FaderWidget的窗体属性为Qt.WA_DeleteOnClose，当整个对话框关闭时，此渐变窗体也同时关闭。
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(parent.size())
        
    def start(self):
        self.currentAlpha = 255
        self.timer.start(100)
        self.show()
        
    def paintEvent(self, event):
        #半透明色
        semiTransparentColor = self.startColor
        semiTransparentColor.setAlpha(self.currentAlpha)
        
        painter = QPainter(self)
        painter.fillRect(self.rect(), semiTransparentColor)
        
        self.currentAlpha -= (255*self.timer.interval()/self.duration)
        
        if self.currentAlpha <= 0:  
            self.timer.stop()  
            self.close() 
            
            
class Model(QSqlTableModel):
    
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        
        self.setTable("Fireworks")
        self.setSort(5, Qt.AscendingOrder)
        self.select()
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
class InsertDialog(QDialog):
    
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.FireworkIDLabel = QLabel("FireworkID:")
        self.IgnitorIDLabel = QLabel("IgnitorID:")
        self.ConnectorIDLabel = QLabel("ConnectorID:")
        self.DurationLabel = QLabel("Duration:")
        self.InventoryLabel = QLabel("Inventory:")
        self.ColorLabel = QLabel("Color:")
        self.AngleLabel = QLabel("Angle:")

        self.FireworkIDEidt = QLineEdit()
        self.IgnitorIDEidt = QLineEdit()
        self.ConnectorIDEidt = QLineEdit()
        self.DurationEidt = QLineEdit()
        self.InventoryEidt = QLineEdit()
        self.ColorEidt = QLineEdit()
        self.AngleEidt = QLineEdit()
        
        self.saveButton = QPushButton("Save")
        self.cancelButton = QPushButton("Cancel")
        
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.saveButton)
        self.hbox.addWidget(self.cancelButton)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.FireworkIDLabel, 0, 0)
        self.layout.addWidget(self.FireworkIDEidt, 0, 1)
        self.layout.addWidget(self.IgnitorIDLabel, 1, 0)
        self.layout.addWidget(self.IgnitorIDEidt, 1, 1)
        self.layout.addWidget(self.ConnectorIDLabel, 2, 0)
        self.layout.addWidget(self.ConnectorIDEidt, 2, 1)
        self.layout.addWidget(self.DurationLabel, 3, 0)
        self.layout.addWidget(self.DurationEidt, 3, 1)
        self.layout.addWidget(self.InventoryLabel, 4, 0)
        self.layout.addWidget(self.InventoryEidt, 4, 1)
        self.layout.addWidget(self.ColorLabel, 5, 0)
        self.layout.addWidget(self.ColorEidt, 5, 1)
        self.layout.addWidget(self.AngleLabel, 6, 0)
        self.layout.addWidget(self.AngleEidt, 6, 1)
        self.layout.addLayout(self.hbox, 8, 0, 1, 2)
        self.setLayout(self.layout)
        
        self.saveButton.clicked.connect(self.saveData)
        self.cancelButton.clicked.connect(self.cancel)
        
        self.op = OperationDatabase()
        
    def saveData(self):
        self.op.insertData(self.FireworkIDEidt.text(), self.IgnitorIDEidt.text(),self.ConnectorIDEidt.text(),self.DurationEidt.text(),self.InventoryEidt.text(),self.ColorEidt.text(),self.AngleEidt.text())
        self.FireworkIDEidt.setText("")
        self.IgnitorIDEidt.setText("")
        self.ConnectorIDEidt.setText("")
        self.DurationEidt.setText("")
        self.InventoryEidt.setText("")
        self.ColorEidt.setText("")
        self.AngleEidt.setText("")
        
    def cancel(self):
        self.close()
        
class FireworkInfo(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.view = QTableView(self)
        self.model = Model(self.view)
        self.view.setModel(self.model)
        self.op = OperationDatabase()
        self.view.resize(800, 300)
        
#        self.addButton = QPushButton("InsertData")
#        vbox = QVBoxLayout()
#        vbox.addWidget(self.view)
#        vbox.addWidget(self.addButton)
#        self.setLayout(vbox)
#        self.addButton.clicked.connect(self.add)
        
        #设置右键菜单
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
    #右键菜单函数
    @Slot(QPoint)    
    def on_view_customContextMenuRequested(self, point):
        
        rightMenu = QMenu(self)
        insertDataAction = QAction("Insert", self)
        insertDataAction.setStatusTip("Insert a line below the selected line")
        insertDataAction.connect(SIGNAL("triggered()"), self.add)
        rightMenu.addAction(insertDataAction)
        rightMenu.exec_(QCursor.pos())
        
    def add(self):
        insertDialog = InsertDialog()
        insertDialog.show()

class Combination(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.view = QTableView(self)
        self.model = QStandardItemModel (0, 3, self)
        self.model.setHorizontalHeaderLabels(["ID", "FireworkID", "Duration"])
        self.view.setModel(self.model)
        self.view.resize(800, 300)

class Script(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.view = QTableView(self)
        self.model = QStandardItemModel (0, 3, self)
        self.model.setHorizontalHeaderLabels(["ID", "FireworkID", "Amount", "Location"])
        self.view.setModel(self.model)
        self.view.resize(800, 300)
        
        




if __name__ == "__main__" : 
    app=QApplication(sys.argv) 
    createConnection() 
    demo=StockDiaog()  
    demo.show()  
    sys.exit(app.exec_()) 
