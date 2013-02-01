#coding=utf-8
'''
Created on 2013-1-31

@author: pyroshow
'''

import sys
from resources import rc_picture
from PySide.QtGui import *
from PySide.QtCore import *
from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from toolKit import mergeDelegate
from toolKit.mergeDelegate import MergeDelegate

engine = create_engine("sqlite:///pyro.db")
session = scoped_session(sessionmaker(bind = engine, autocommit= True))
base = declarative_base()


class Data(base):
    
    __tablename__ = "Data"
    
    id = Column(Integer, Sequence("session_id_seq"), primary_key = True)
    type = Column(String)
    item = Column(String)
    description = Column(String)
    size = Column(String)
    stock = Column(String)
    used_effects = Column(String)
    rising_time = Column(String)
    effect = Column(String)
    c = Column(String)
    angle = Column(String)
    
    def __init__(self, type = None, item = None, description = None, 
                 size = None, stock = None, used_effects = None, 
                 rising_time = None, effect = None, c = None, angle = None):
        self.type = type
        self.item = item
        self.description = description
        self.size = size
        self.stock = stock
        self.used_effects = used_effects
        self.rising_time = rising_time
        self.effect = effect
        self.c = c
        self.angle = angle
        
        
class MyTestDialog(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.setWindowIcon(QIcon(":/images/title.png"))
        
        self.setWindowTitle("My Database Dialog")
        
        self.typeLabel = QLabel("Type:")
        self.itemLabel = QLabel("Item:")
        self.descriptionLabel = QLabel("Description:")
        self.sizeLabel = QLabel("Size:")
        self.stockLabel = QLabel("Stock:")
        self.usedEffectsLabel = QLabel("Used Effects:")
        self.risingTimeLabel = QLabel("Rising Time:")
        self.effectLabel = QLabel("Effect:")
        self.colorLabel = QLabel("Color:")
        self.angleLabel = QLabel("Angle:")

        self.typeEidt = QLineEdit()
        self.itemEidt = QLineEdit()
        self.descriptionEidt = QLineEdit()
        self.sizeEidt = QLineEdit()
        self.stockEidt = QLineEdit()
        self.usedEffectsEidt = QLineEdit()
        self.risingTimeEidt = QLineEdit()
        self.effectEidt = QLineEdit()
        self.colorEidt = QLineEdit()
        self.angleEidt = QLineEdit()
        
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.typeLabel)
        hbox1.addWidget(self.typeEidt)
        hbox1.addWidget(self.itemLabel)
        hbox1.addWidget(self.itemEidt)
        hbox1.addWidget(self.descriptionLabel)
        hbox1.addWidget(self.descriptionEidt)
        hbox1.addWidget(self.sizeLabel)
        hbox1.addWidget(self.sizeEidt)
        hbox1.addWidget(self.stockLabel)
        hbox1.addWidget(self.stockEidt)
        
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.usedEffectsLabel)
        hbox2.addWidget(self.usedEffectsEidt)
        hbox2.addWidget(self.risingTimeLabel)
        hbox2.addWidget(self.risingTimeEidt)
        hbox2.addWidget(self.effectLabel)
        hbox2.addWidget(self.effectEidt)
        hbox2.addWidget(self.colorLabel)
        hbox2.addWidget(self.colorEidt)
        hbox2.addWidget(self.angleLabel)
        hbox2.addWidget(self.angleEidt)
        
        self.insertButton = QPushButton("Insert")
        self.queryButton = QPushButton("Query")
        self.clearButton = QPushButton("Clear")

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.insertButton)
        hbox3.addWidget(self.queryButton)
        hbox3.addWidget(self.clearButton)
        
        vbox = QVBoxLayout()
        
        tabWidget = QTabWidget()
        
        self.view1 = QTableView()
        self.view1.setAutoScroll(False)
        self.view1.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view1.setSelectionMode(QAbstractItemView.SingleSelection)
        #设置交互颜色
        self.view1.setAlternatingRowColors (True)
        #行和列显示都按内容来
        self.view1.resizeColumnsToContents()
        self.view1.resizeRowsToContents()
        #对model进行操作
        #
        self.model = QStandardItemModel (0, 10, self)
        self.model.setHorizontalHeaderLabels (["Type", "Item", "Description", "Size", "Stock", "Used Effects", "Rising Time", "Effect", "Color", "Angel"])
        self.view1.setModel (self.model)
        
        self.view1.setItemDelegate(MergeDelegate(self))
        
        
        #设置右键菜单
        self.view1.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view1.customContextMenuRequested.connect(self.on_view1_customContextMenuRequested)

        #设置tableView里面model左键编辑修改事件
        self.model.itemChanged.connect(self.changeData)
        
        self.view2 = QTableView()
        self.view2.setAutoScroll(False)
        self.view2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view2.setAlternatingRowColors (True)
        self.view2.resizeColumnsToContents()
        self.view2.resizeRowsToContents()
        
        self.view2.setModel (self.model)
        
        self.view2.setItemDelegate(MergeDelegate(self))
        
        
        self.view3 = QTableView()
        self.view3.setAutoScroll(False)
        self.view3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view3.setAlternatingRowColors (True)
        self.view3.resizeColumnsToContents()
        self.view3.resizeRowsToContents()
        
        self.view3.setModel (self.model)
        
        self.view3.setItemDelegate(MergeDelegate(self))
        
        
        self.view4 = QTableView()
        self.view4.setAutoScroll(False)
        self.view4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view4.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view4.setAlternatingRowColors (True)
        self.view4.resizeColumnsToContents()
        self.view4.resizeRowsToContents()
        
        self.view4.setModel (self.model)
        
        self.view4.setItemDelegate(MergeDelegate(self))
        
        self.view5 = QTableView()
        self.view5.setAutoScroll(False)
        self.view5.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view5.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view5.setAlternatingRowColors (True)
        self.view5.resizeColumnsToContents()
        self.view5.resizeRowsToContents()
        
        self.view5.setModel (self.model)
        
        self.view5.setItemDelegate(MergeDelegate(self))
        
        self.view6 = QTableView()
        self.view6.setAutoScroll(False)
        self.view6.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view6.setSelectionMode(QAbstractItemView.SingleSelection)
        self.view6.setAlternatingRowColors (True)
        self.view6.resizeColumnsToContents()
        self.view6.resizeRowsToContents()
        
        self.view6.setModel (self.model)
        
        self.view6.setItemDelegate(MergeDelegate(self))
        
        tabWidget.addTab(self.view1, "Database1")
        tabWidget.addTab(self.view2, "Database2")
        tabWidget.addTab(self.view3, "Database3")
        tabWidget.addTab(self.view4, "Database4")
        tabWidget.addTab(self.view5, "Database5")
        tabWidget.addTab(self.view6, "Database6")
        
        vbox.addWidget(tabWidget)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        self.setLayout(vbox)
        
        self.insertButton.clicked.connect(self.insert)
        self.queryButton.clicked.connect(self.query)
        self.clearButton.clicked.connect(self.clear)
        
        base.metadata.create_all(engine)
        self.sess = session()
        
    def insert(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to insert data to database?', QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            with self.sess.begin():
                record = Data()
                record.type = self.typeEidt.text()
                record.item = self.itemEidt.text()
                record.description = self.descriptionEidt.text()
                record.size = self.sizeEidt.text()
                record.stock = self.stockEidt.text()
                record.used_effects = self.usedEffectsEidt.text()
                record.rising_time = self.risingTimeEidt.text()
                record.effect = self.effectEidt.text()
                record.c = self.colorEidt.text()
                record.angle = self.angleEidt.text()

                self.sess.add(record)

            self.typeEidt.setText("")
            self.itemEidt.setText("")
            self.descriptionEidt.setText("")
            self.sizeEidt.setText("")
            self.stockEidt.setText("")
            self.usedEffectsEidt.setText("")
            self.risingTimeEidt.setText("")
            self.effectEidt.setText("")
            self.colorEidt.setText("")
            self.angleEidt.setText("")
        else:
            pass  

    def query(self):
        self.clear()
        with self.sess.begin():
            record = self.sess.query (Data).all()
            
            for row in record:
                newrow = []
                newrow.append (QStandardItem (row.type))
                newrow.append (QStandardItem (row.item))
                newrow.append (QStandardItem (row.description))
                newrow.append (QStandardItem (row.size))
                newrow.append (QStandardItem (row.stock))
                newrow.append (QStandardItem (row.used_effects))
                newrow.append (QStandardItem (row.rising_time))
                newrow.append (QStandardItem (row.effect))
                newrow.append (QStandardItem (row.c))
                newrow.append (QStandardItem (row.angle))
            
                #为model添加行数据
                self.model.appendRow (newrow)


    def clear(self):
        self.typeEidt.setText("")
        self.itemEidt.setText("")
        self.descriptionEidt.setText("")
        self.sizeEidt.setText("")
        self.stockEidt.setText("")
        self.usedEffectsEidt.setText("")
        self.risingTimeEidt.setText("")
        self.effectEidt.setText("")
        self.colorEidt.setText("")
        self.angleEidt.setText("")
            #清空model
        self.model.clear()
        self.model.setHorizontalHeaderLabels (["Type", "Item", "Description", "Size", "Stock", "Used Effects", "Rising Time", "Effect", "Color", "Angel"])
        
        
        
    #右键槽函数
    @Slot(QPoint)
    def on_view1_customContextMenuRequested(self, point):
        
        rightMenu = QMenu(self)
        closeAction = QAction(self.tr('Close'), self, triggered = self.close)
        rightMenu.addAction(closeAction)
        rightMenu.exec_(QCursor.pos())


    #左击槽函数
    @Slot(QStandardItem)
    def changeData(self, item):
        data = item.text()
        row = item.row()
        column = item.column()
        reply = QMessageBox.question(self, 'Confirm', "Are you sure to update the data?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.update(data, row, column)
        else:
            self.query()
            
    #更新数据库
    def update(self, data, row, column):
        with self.sess.begin():
            q = self.sess.query(Data)

            record = q.all()[row]
            if column == 0:
                record.type = data
            elif column == 1:
                record.item = data
            elif column == 2:
                record.description = data
            elif column == 3:
                record.size= data
            elif column == 4:
                record.stock = data
            elif column == 5:
                record.used_effects = data
            elif column == 6:
                record.rising_time = data
            elif column == 7:
                record.effect = data
            elif column == 8:
                record.c = data
            elif column == 9:
                record.angle = data
                
        self.query()
                
            
    

app = QApplication(sys.argv)
dlg = MyTestDialog()
dlg.show()
sys.exit(app.exec_())
        





