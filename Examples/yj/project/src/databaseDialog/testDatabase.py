'''
Created on 2013-1-31

@author: pyroshow
'''


import sys
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtSql import *
from resources import rc_picture

 

def createConnection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("my.db")
    db.open()

class OperationDatabase():
    
    def __init__(self):
        self.q = QSqlQuery() 
        self.q.exec_(u"create table if not exists TBL1(id integer primary key autoincrement, name varchar(20) not null, sex varchar(4) not null, age integer not null, stature integer not null)")
        self.q.exec_("commit")
            
    def insertData(self, *value):
        self.q.prepare("insert into TBL1(name, sex, age, stature) values(?, ?, ?, ?)")
        self.q.bindValue(0, value[0])
        self.q.bindValue(1, value[1])
        self.q.bindValue(2, value[2])
        self.q.bindValue(3, value[3])
        self.q.exec_()
        self.q.exec_("commit")



class Model(QSqlTableModel):
    
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        
        self.setTable("TBL1")
        self.setSort(3, Qt.AscendingOrder)
        self.select()
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
        
class Widget(QDialog):
    
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        
        
        self.setWindowIcon(QIcon(":/images/title.png"))
        self.setWindowTitle("Testing...")
        self.resize(600, 400)
        
        
        self.nameLabel = QLabel("Name:")
        self.sexLabel = QLabel("Sex:")
        self.ageLabel = QLabel("Age:")
        self.statureLabel = QLabel("Stature:")

        self.nameEidt = QLineEdit()
        self.sexEidt = QLineEdit()
        self.ageEidt = QLineEdit()
        self.statureEidt = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.nameLabel)
        hbox1.addWidget(self.nameEidt)
        hbox1.addWidget(self.sexLabel)
        hbox1.addWidget(self.sexEidt)
        hbox1.addWidget(self.ageLabel)
        hbox1.addWidget(self.ageEidt)
        hbox1.addWidget(self.statureLabel)
        hbox1.addWidget(self.statureEidt)
        
        
        self.insertButton = QPushButton("Insert Data")
        self.updateButton = QPushButton("Update Show")
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.insertButton)
        hbox2.addWidget(self.updateButton)
        
        tabWidget = QTabWidget()
        self.view1 = QTableView(self)
        self.view2 = QTableView(self)
        self.view3 = QTableView(self)
        self.view4 = QTableView(self)
        self.view5 = QTableView(self)
        self.view6 = QTableView(self)
        
        self.model = Model(self.view1)
        self.model2 = Model(self.view2)
        self.model3 = Model(self.view3)
        self.model4 = Model(self.view4)
        self.model5 = Model(self.view5)
        self.model6 = Model(self.view6)
        
        self.view1.setModel(self.model)
        self.view2.setModel(self.model2)
        self.view3.setModel(self.model3)
        self.view4.setModel(self.model4)
        self.view5.setModel(self.model5)
        self.view6.setModel(self.model6)
        
        tabWidget.addTab(self.view1, "Database1")
        tabWidget.addTab(self.view2, "Database2")
        tabWidget.addTab(self.view3, "Database3")
        tabWidget.addTab(self.view4, "Database4")
        tabWidget.addTab(self.view5, "Database5")
        tabWidget.addTab(self.view6, "Database6")
        vbox = QVBoxLayout()
        vbox.addWidget(tabWidget)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        
        self.op = OperationDatabase()
        self.insertButton.clicked.connect(self.insert)
        self.updateButton.clicked.connect(self.updateShow)
        
    def insert(self):
        self.op.insertData(self.nameEidt.text(), self.sexEidt.text(), int(self.ageEidt.text()), int(self.statureEidt.text()))
        self.nameEidt.setText("")
        self.sexEidt.setText("")
        self.ageEidt.setText("")
        self.statureEidt.setText("")
        
        
    def updateShow(self):
        self.model.select()
        self.model2.select()
        self.model3.select()
        self.model4.select()
        self.model5.select()
        self.model6.select()

        
if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    createConnection()
    test = Widget()
    test.show()
    sys.exit(app.exec_())



