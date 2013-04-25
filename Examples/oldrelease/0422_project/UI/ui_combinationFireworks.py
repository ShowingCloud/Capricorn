#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from Delegate.combinationDelegate import CombinationDelegate
from Models.LocalDB import *
from PySide.QtCore import *
from PySide.QtGui import *
from UI.ui_chooseFieldNew import ChooseField
import json
from datetime import timedelta


class Combination(QWidget):

    def __init__(self, sess, session, musicSignal, parent = None):
        QWidget.__init__(self, parent)
        
        self.sourceGroupBox = QGroupBox("Combination")
        self.view = QTableView(self)
        self.view.setAutoScroll(True)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.view.setSelectionMode(QAbstractItemView.SingleSelection)
        #设置交互颜色
        self.view.setAlternatingRowColors (True)
        #行和列显示都按内容来
        self.view.resizeColumnsToContents()
        self.view.resizeRowsToContents()
        self.model = QStandardItemModel (0, 4, self)
        self.model.setHorizontalHeaderLabels(["UUID", "ID", "Contents", "Total Time (sec)"])
        
        self.sess = sess
        self.session = session
        self.musicSignal = musicSignal
        self.signalTime = None
        self.query()
        self.view.setItemDelegate(CombinationDelegate(self.sess, self))   
        self.view.setModel(self.model)
        self.view.hideColumn(0)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        
        self.sourceGroupBox.setLayout(vbox)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.sourceGroupBox)
        
        self.setLayout(mainLayout)
        
        self.resize(1060, 500)
        
    #设置右键菜单
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置右键菜单函数
        self.view.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
    #右键菜单函数
    @Slot(QPoint)    
    def on_view_customContextMenuRequested(self, point):
        
        #获得当前的选中列
        self.column = self.view.columnAt(point.x())
        self.row = self.view.rowAt(point.y())
        rightMenu = QMenu(self)
        refreshAction = QAction("Refresh", self)
        refreshAction.setStatusTip("Refresh the fireworks from  database")
        refreshAction.connect(SIGNAL("triggered()"), self.refresh)
        rightMenu.addAction(refreshAction)
        if self.row >= 0:
            deleteAction = QAction("Delete", self)
            deleteAction.setStatusTip("Delete selected line")
            deleteAction.connect(SIGNAL("triggered()"), self.delete)
            rightMenu.addAction(deleteAction)
            
            scriptAction = QAction("Add to script", self)
            scriptAction.setStatusTip("Add  fireworks to the script")
            scriptAction.connect(SIGNAL("triggered()"), self.addScriptFireworks)
            rightMenu.addAction(scriptAction)
        rightMenu.exec_(QCursor.pos())
        
    def query(self):
        with self.sess.begin():
            
            record = self.sess.query (FireworksData).filter_by(Type = 'Combination').all()
        for row in record:
            newrow = []
            info = json.loads(row.Combination)
            k = info.keys()
            newrow.append (QStandardItem (row.UUID))
            newrow.append (QStandardItem (k[0]))
            num = len(info[k[0]])
            con = '('+str(num)+')'
            con1 = ''
            for i in range(num):
                con1 += ','+info[k[0]][i][0]
                    
                
            newrow.append (QStandardItem (con+con1))
            newrow.append (QStandardItem (str(info[k[0]][num-1][1])))
                
            #为model添加行数据
            self.model.appendRow (newrow)
                
    def refresh(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["UUID", "ID", "Contents", "Total Time (sec)"])
        self.query()
        self.view.hideColumn(0)
        
    def delete(self):
        item = self.model.item(self.row)
        with self.sess.begin():
            record = self.sess.query (FireworksData).filter_by(UUID = item.text()).first()
            #删除表格里面数据
            self.model.takeRow(self.row)
            #删除数据库里面的数据
            self.sess.delete(record)
            
    @Slot(int)
    def getTime(self, signalTime):
        
        self.signalTime = signalTime
        
    
    

        
    @Slot()
    def addScriptFireworks(self):
        item = self.model.item(self.row, 0)
        if self.signalTime != None:
            effectTime = timedelta(microseconds = self.signalTime*1000)
        else:
            effectTime = timedelta(microseconds = 0)
        chooseField = ChooseField(self.sess, self.session,  item.text(), effectTime, self.musicSignal, self)
        acc = chooseField.exec_()



