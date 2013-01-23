#!/usr/bin/python
#_*_encoding:utf-8_*_

#myTableView.py

from PySide.QtGui import *
from PySide.QtCore import *

import sys
import my_resouces

from PySide import QtGui, QtCore, QtSql
from sqlalchemy import Column, Integer, Sequence, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from datetime import datetime

engine = create_engine('sqlite:///testsql.db')
session = scoped_session(sessionmaker(bind = engine, autocommit = True))
base = declarative_base()

class Data(base):
    __tablename__ = 'Data'

    id = Column(Integer, Sequence('session_id_seq'), primary_key = True)
    name = Column(String)
    addr = Column(String)
    tel = Column(String)
    salary = Column(String)
    time = Column(DateTime)

    def __init__(self, name = None, addr = None, tel = None, salary = None, time = None):
        self.name = name
        self.addr = addr
        self.tel = tel
        self.salary = salary
        self.time = time


class TestDatabase(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Pyro Show Media Contact")
        self.resize(430, 300)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/images/preview.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        self.setToolTip("This is Pyro Show Media staff information sheet.")
        QtGui.QToolTip.setFont(QtGui.QFont('oldEnglish', 12))

        self.nameLabel = QtGui.QLabel("Name:")
        self.telLabel = QtGui.QLabel("Tel:")
        self.addrLabel = QtGui.QLabel("Addr:")
        self.salaryLabel = QtGui.QLabel("Salary:")

        self.nameEidt = QtGui.QLineEdit()
        self.telEidt = QtGui.QLineEdit()
        self.addrEidt = QtGui.QLineEdit()
        self.salaryEidt = QtGui.QLineEdit()

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.nameLabel)
        hbox.addWidget(self.nameEidt)
        hbox.addWidget(self.addrLabel)
        hbox.addWidget(self.addrEidt)
        hbox.addWidget(self.telLabel)
        hbox.addWidget(self.telEidt)
        hbox.addWidget(self.salaryLabel)
        hbox.addWidget(self.salaryEidt)

        self.tableView = QTableView()
        self.tableView.setAutoScroll(False)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setAlternatingRowColors (True)
        #设置选中一行
##        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()

        # COLUMNS是列数，初始时行数是0
        # 下面的COLUMN1, COLUMN2, ...是每一列的标题
	# setModel只要在开始的时候调用一次就够了
        self.model = QtGui.QStandardItemModel (0, 3, self)
        self.model.setHorizontalHeaderLabels (["Name", "Addr", "Tel", "Salary"])
        self.tableView.setModel (self.model)
        
        self.insertButton = QtGui.QPushButton("Insert")
        self.queryButton = QtGui.QPushButton("Query")
        self.clearButton = QtGui.QPushButton("Clear")

        hButtonLayout = QtGui.QHBoxLayout()
        hButtonLayout.addWidget(self.insertButton)
        hButtonLayout.addWidget(self.queryButton)
        hButtonLayout.addWidget(self.clearButton)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.tableView)
        layout.addLayout(hButtonLayout)
        self.setLayout(layout)

        self.center()

        self.insertButton.clicked.connect(self.insert)
        self.queryButton.clicked.connect(self.query)
        self.clearButton.clicked.connect(self.clear)
        #设置右键菜单
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.on_tableView_customContextMenuRequested)

        base.metadata.create_all(engine)
        self.sess = session()


    def insert(self):
        reply = QtGui.QMessageBox.question(self, 'Message', 'Are you sure to insert data to database?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            with self.sess.begin():
                record = Data()
                record.name = self.nameEidt.text()
                record.tel = self.telEidt.text()
                record.salary = self.salaryEidt.text()
                record.addr = self.addrEidt.text()
                record.time = datetime.now()

                self.sess.add(record)

            self.nameEidt.setText("")
            self.addrEidt.setText("")
            self.telEidt.setText("")
            self.salaryEidt.setText("")
        else:
            pass  

    def query(self):
        self.clear()
        with self.sess.begin():
            record = self.sess.query (Data).all()
            
            for row in record:
                newrow = []
                newrow.append (QtGui.QStandardItem (row.name))
                newrow.append (QtGui.QStandardItem (row.addr))
                newrow.append (QtGui.QStandardItem (row.tel))
                newrow.append (QtGui.QStandardItem (row.salary))
                #为model添加行数据
                self.model.appendRow (newrow)

            self.nameEidt.setText("All")
            self.addrEidt.setText("Data")
            self.telEidt.setText("As")
            self.salaryEidt.setText("Follows!")

    def clear(self):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to clear the tableView's data?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.nameEidt.setText("")
            self.addrEidt.setText("")
            self.telEidt.setText("")
            self.salaryEidt.setText("")
            #清空model
            self.model.clear()
            self.model.setHorizontalHeaderLabels (["Name", "Addr", "Tel", "Salary"])
        else:
            pass

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message', 'Are you sure to quit?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
    
    #为什么我的右键不响应？
    @QtCore.Slot(QtCore.QPoint)
    def on_tableView_customContextMenuRequested(self, point):
        print 1
        rightMenu = QtGui.QMenu(self)
        closeAction = QtGui.QAction(self.tr('Close'), self, triggered = self.close)
        rightMenu.addAction(closeAction)
        rightMenu.exec_(QtGui.QCursor.pos())

##    def showContextMenu(self, pos):
##        self.tableView.rightMenu.move(self.pos() + pos)
##        self.tableView.rightMenu.show()
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = TestDatabase()
    window.show()
    sys.exit(app.exec_())
        
        
        
