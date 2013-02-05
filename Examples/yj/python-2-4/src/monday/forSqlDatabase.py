#coding=utf-8
'''
Created on 2013-2-4

@author: pyroshow
'''

import sys
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtSql import *


def createConnection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    db.open()
    
def createTable():
    q = QSqlQuery()
    q.exec_("create table if not exists info(id integer primary key autoincrement, name varchar(20) not null, sex varchar(4) not null, age integer not null, stature integer not null)")
    
    q.prepare("insert into info(name, sex, age, stature) values(?, ?, ?, ?)")
    q.bindValue(0, "YuJin")
    q.bindValue(1, u"男")
    q.bindValue(2, 27)
    q.bindValue(3, 170)
    q.exec_()
    q.exec_("commit")
    
class Model(QSqlTableModel):
    
    def __init__(self, parent = None):
        QSqlTableModel.__init__(self, parent)
        
        self.setTable("info")
        self.select()
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
        
class Demo(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.setWindowTitle("Demo")
        self.setGeometry(300, 300, 500, 300)
        vbox = QVBoxLayout(self)
        self.view = QTableView(self)
        self.model = Model(self)
        self.view.setModel(self.model)
        vbox.addWidget(self.view)
        
        
        
app = QApplication(sys.argv)
createConnection()
createTable()
demo = Demo()
demo.show()
sys.exit(app.exec_())

        




