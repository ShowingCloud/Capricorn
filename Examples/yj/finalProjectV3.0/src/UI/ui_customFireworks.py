#coding=utf-8
'''
Created on 2013-3-7

@author: pyroshow
'''
from Delegate.customDelegate import CustomDelegate
from Models.LocalDB import *
from PySide.QtCore import *
from PySide.QtGui import *
from UI.ui_chooseFieldNew import ChooseField

class Custom(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.mainGroupBox = QGroupBox("Fireworks")
        
        self.model = QStandardItemModel (0, 15, self)
        self.model.setHorizontalHeaderLabels (["UUID", "Name", "Alias", "Size", "Used Effects", "Rising Time", "Stock", "Weight Net", "Weight Gross", "Application", "Safety Distance Horizontal", "Safety Distance Vertical", "Information", "Price", "Notes"])
        
        self.proxyView = QTableView(self)
        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyModel.setSourceModel(self.model)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)
        self.proxyView.setItemDelegate(CustomDelegate(self))
        
        #隐藏第一列的值
        self.proxyView.hideColumn(0)
        
        self.filterPatternLineEdit = QLineEdit()
        self.filterPatternLineEdit.setText("")
        self.filterPatternLabel = QLabel("&Filter pattern:")
        self.filterPatternLabel.setBuddy(self.filterPatternLineEdit)


        self.filterColumnComboBox = QComboBox()
        self.filterColumnComboBox.addItems(["Name", "Alias", "Size", "Used Effects", "Rising Time", "Stock", "Weight Net", "Weight Gross", "Application", "Safety Distance Horizontal", "Safety Distance Vertical", "Information", "Price", "Notes"])
        self.filterColumnLabel = QLabel("Filter &column:")
        self.filterColumnLabel.setBuddy(self.filterColumnComboBox)

        self.filterPatternLineEdit.textChanged.connect(self.filterRegExpChanged)
        self.filterColumnComboBox.currentIndexChanged.connect(self.filterColumnChanged)
        
        tabLayout = QHBoxLayout()
        tabLayout.addStretch(1)
        tabLayout.addWidget(self.filterPatternLabel)
        tabLayout.addWidget(self.filterPatternLineEdit)
        tabLayout.addWidget(self.filterColumnLabel)
        tabLayout.addWidget(self.filterColumnComboBox)
        
        
                
        self.proxyView.sortByColumn(0, Qt.AscendingOrder)
        self.filterColumnComboBox.setCurrentIndex(6)
        
        fireworksLayout = QVBoxLayout()
        fireworksLayout.addLayout(tabLayout)
        fireworksLayout.addWidget(self.proxyView)
        
        self.mainGroupBox.setLayout(fireworksLayout)
        
        self.headView = self.proxyView.horizontalHeader()
        self.headView.sectionClicked.connect(self.ascendingSort)
        self.headView.sectionDoubleClicked.connect(self.descendingSort)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.mainGroupBox)
        self.setLayout(mainLayout)
        self.resize(1060, 500)
        
        self.sess = session()
        self.query()
        
        #设置右键菜单
        self.proxyView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.proxyView.customContextMenuRequested.connect(self.on_view_customContextMenuRequested)
        
    #右键菜单函数
    @Slot(QPoint)    
    def on_view_customContextMenuRequested(self, point):
        
        #获得当前的选中列
        self.column = self.proxyView.columnAt(point.x())
        self.row = self.proxyView.rowAt(point.y())
        rightMenu = QMenu(self)
        if self.row >= 0:
            showMoreAction = QAction("Show more ...", self)
            showMoreAction.setStatusTip("Show  the fireworks more information")
            showMoreAction.connect(SIGNAL("triggered()"), self.showMoreInfo)
            rightMenu.addAction(showMoreAction)
            
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
            record = self.sess.query (FireworksData).filter_by(Type = "Custom").all()
            
            for row in record:
                newrow = []
                newrow.append (QStandardItem (row.UUID))
                newrow.append (QStandardItem (row.Name))
                newrow.append (QStandardItem (row.Alias))
                newrow.append (QStandardItem (str(row.Size)))
                newrow.append (QStandardItem (str(row.UsedEffects)))
                newrow.append (QStandardItem (str(row.RisingTime)))
                newrow.append (QStandardItem (str(row.Stock)))
                newrow.append (QStandardItem (str(row.WeightNet)))
                newrow.append (QStandardItem (str(row.WeightGross)))
                if row.Indoor == 0:
                    newrow.append (QStandardItem ("Indoor"))
                elif row.Indoor == 1:
                    newrow.append (QStandardItem ("Outdoor"))
                newrow.append (QStandardItem (str(row.SDHorizontal)))
                newrow.append (QStandardItem (str(row.SDVertical)))
                newrow.append (QStandardItem (row.Information))
                newrow.append (QStandardItem (str(row.Price)))
                newrow.append (QStandardItem (row.Notes))
                
                self.model.appendRow (newrow)
        
    @Slot(int)
    def ascendingSort(self, index):
        self.model.sort(index, Qt.AscendingOrder)
        
    @Slot(int)
    def descendingSort(self, index):
        self.model.sort(index, Qt.DescendingOrder)
        
    def addScriptFireworks(self):
        item = self.model.item(self.row, 0)
        chooseField = ChooseField( item.text(), self)
        acc = chooseField.exec_()

    def showMoreInfo(self):
        pass
    
    def delete(self):
        item = self.model.item(self.row)
        with self.sess.begin():
            record = self.sess.query (FireworksData).filter_by(UUID = item.text()).first()
            #删除表格里面数据
            self.model.takeRow(self.row)
            #删除数据库里面的数据
            self.sess.delete(record)
        
        
    def filterRegExpChanged(self):
        pass
        regExp = QRegExp(self.filterPatternLineEdit.text())
        self.proxyModel.setFilterRegExp(regExp)

    def filterColumnChanged(self):
        pass
        
        '''
        remarks: Because hidden a line so to plus one
        '''
        self.proxyModel.setFilterKeyColumn(self.filterColumnComboBox.currentIndex()+1)



