#coding=utf-8
'''
Created on 2013-2-22

@author: pyroshow
'''

from PySide.QtGui import *
from PySide.QtCore import *
from toolKit.combinationDelegate import CombinationDelegate
from alchemy.AlchemyOpereation import *
import json


class Combination(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.view = QTableView(self)
        self.view.resizeColumnsToContents()
        self.model = QStandardItemModel (3, 1, self)
        self.model.setHorizontalHeaderLabels(["ID", "Combination Info(Item/Time)"])
        
        self.sess = session()
        base.metadata.create_all(engine)
        self.query()
        self.view.setItemDelegate(CombinationDelegate(self))   
        self.view.setModel(self.model)
        self.view.resize(960, 300)
        
    def query(self):
        with self.sess.begin():
            record = self.sess.query (Data).all()
            
            
            for row in record:
                newrow = []
                if row.Type == 'Combination' :
                    
                    info = json.loads(row.Combination)
                    k = info.keys()
                    newrow.append (QStandardItem (k[0]))
                    newrow.append (QStandardItem (str(info[k[0]])))
                
                    #为model添加行数据
                    self.model.appendRow (newrow)
                
                
                