#coding=utf-8
'''
Created on 2013-3-6

@author: pyroshow
'''

from Delegate.mergeDelegate import MergeDelegate
from Models.LocalDB import *
from PySide.QtCore import *
from PySide.QtGui import *
from UI.ui_DatabaseEditShow import uiShow
from UI.ui_DatabaseShowMore_Show import uiShowMore
from UI.ui_aliasAndNotes import ModifyAliasNotes
from UI.ui_chooseFieldNew import ChooseField
from UI.ui_combinationAddPopupWindow import CombinationDialog
from datetime import timedelta

class Fireworks(QWidget):
    
    def __init__(self, Type, sess, session,  musicSignal, parent = None):
        QWidget.__init__(self, parent)
        
        
        self.sess = sess
        self.Type = Type
        self.session = session
        self.signalTime = None
        self.musicSignal = musicSignal
        self.mainGroupBox = QGroupBox("Fireworks")
        self.mainGroupBox.setContentsMargins(0, 0, 0, 0)
        
        self.model = QStandardItemModel (0, 15, self)
        self.model.setHorizontalHeaderLabels (["UUID","Size (mm)", "Supplier", "Name", "Alias", "Rising Time", "Stock", "Weight Net", "Weight Gross", "Application", "Safety Distance Horizontal", "Safety Distance Vertical", "Information", "Price", "Notes"])
        
        self.proxyView = QTableView(self)
        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyModel.setSourceModel(self.model)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)
        self.proxyView.setItemDelegate(MergeDelegate(self.sess, self))
        #设置框格的样式
#        self.proxyView.setGridStyle(Qt.DotLine)
        
        #隐藏第一列的值
        self.proxyView.hideColumn(0)
        
        self.filterPatternLineEdit = QLineEdit()
        self.filterPatternLineEdit.setText("")
        self.filterPatternLabel = QLabel("&Filter pattern:")
        self.filterPatternLabel.setBuddy(self.filterPatternLineEdit)
        
        self.sizeComboBox = QComboBox()
        self.sizeComboBox.addItems(['All', '0.5', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '12'])
        self.sizeLabel = QLabel("<b>Size (inch):</b>")
        self.sizeLabel.setBuddy(self.sizeComboBox)
        
        self.supplierComboBox = QComboBox()
        self.supplierComboBox.addItems(["All", "ShangHai", "BeiJing", "ShenZhen", "GuangZhou"])
        self.supplierLabel = QLabel("<b>Supplier:</b>")
        self.supplierLabel.setBuddy(self.supplierComboBox)

        self.filterColumnComboBox = QComboBox()
        self.filterColumnComboBox.addItems(["Size", "Supplier", "Name", "Alias", "Rising Time", "Stock", "Weight Net", "Weight Gross", "Application", "Safety Distance Horizontal", "Safety Distance Vertical", "Information", "Price", "Notes"])
        self.filterColumnLabel = QLabel("Filter &column:")
        self.filterColumnLabel.setBuddy(self.filterColumnComboBox)

        self.filterPatternLineEdit.textChanged.connect(self.filterRegExpChanged)
        self.filterColumnComboBox.currentIndexChanged.connect(self.filterColumnChanged)
        
        tabLayout = QHBoxLayout()
        tabLayout.addStretch(1)
        
        tabLayout.addWidget(self.sizeLabel)
        tabLayout.addWidget(self.sizeComboBox)
        tabLayout.addSpacing(30)
        tabLayout.addWidget(self.supplierLabel)
        tabLayout.addWidget(self.supplierComboBox)
        tabLayout.addSpacing(30)
        tabLayout.addWidget(self.filterPatternLabel)
        tabLayout.addWidget(self.filterPatternLineEdit)
        tabLayout.addSpacing(30)
        tabLayout.addWidget(self.filterColumnLabel)
        tabLayout.addWidget(self.filterColumnComboBox)
        
        self.sizeComboBox.currentIndexChanged.connect(self.filterBySize)
        self.supplierComboBox.currentIndexChanged.connect(self.filterBySupplier)
        
        
                
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
        
        self.query(Type)
        
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
        insertDataAction = QAction("Insert to database", self)
        insertDataAction.setStatusTip("Insert the fireworks info into  database")
        insertDataAction.connect(SIGNAL("triggered()"), self.insert)
        rightMenu.addAction(insertDataAction)
        if self.row >= 0:
            showMoreAction = QAction("Show more ...", self)
            showMoreAction.setStatusTip("Show  the fireworks more information")
            showMoreAction.connect(SIGNAL("triggered()"), self.showMoreInfo)
            rightMenu.addAction(showMoreAction)
            
            addEditAction = QAction("Add to combination", self)
            addEditAction.setStatusTip("Add  fireworks to the combination")
            addEditAction.connect(SIGNAL("triggered()"), self.addCombinationFireworks)
            rightMenu.addAction(addEditAction)
            
            scriptAction = QAction("Add to script", self)
            scriptAction.setStatusTip("Add  fireworks to the script")
            scriptAction.connect(SIGNAL("triggered()"), self.addScriptFireworks)
            rightMenu.addAction(scriptAction)
            
            modifyAction = QAction("Modify alias and notes", self)
            modifyAction.setStatusTip("Changed the alias and notes")
            modifyAction.connect(SIGNAL("triggered()"), self.changedAliasNotes)
            rightMenu.addAction(modifyAction)
        
        rightMenu.exec_(QCursor.pos())
        
    def query(self, Type):
        with self.sess.begin():
            record = self.sess.query (FireworksData).filter_by(Type = Type).all()
            
        for row in record:
            newrow = []
            newrow.append (QStandardItem (row.UUID))
            newrow.append (QStandardItem (str(row.Size)))
            newrow.append (QStandardItem (row.Supplier))
            newrow.append (QStandardItem (row.Name))
            newrow.append (QStandardItem (row.Alias))
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
                  
    def insert(self):
        insertDialog = uiShow(self.sess, self)
        accept = insertDialog.exec_()
        if accept == 1:
            self.model.clear()
            self.model.setHorizontalHeaderLabels (["UUID","Size (mm)", "Supplier", "Name", "Alias", "Rising Time", "Stock", "Weight Net", "Weight Gross", "Application", "Safety Distance Horizontal", "Safety Distance Vertical", "Information", "Price", "Notes"])
            self.query(self.Type)
            self.proxyView.hideColumn(0)
        
    @Slot(int)
    def ascendingSort(self, index):
        self.model.sort(index, Qt.AscendingOrder)
        
    @Slot(int)
    def descendingSort(self, index):
        self.model.sort(index, Qt.DescendingOrder)
        
    def addCombinationFireworks(self):
        item = self.model.item(self.row, 3)
        item1 = self.model.item(self.row, 0)
        combinationDialog = CombinationDialog(self.sess, item.text(), item1.text(),self)
        combinationDialog.show()

    def showMoreInfo(self):
        item = self.model.item(self.row, 0)
        showMore = uiShowMore(self.sess, item.text(), self)
        showMore.show()
    
    @Slot(int)
    def getTime(self, signalTime):
        
        self.signalTime = signalTime
        
    @Slot()
    def addScriptFireworks(self):
#        self.musicSignal.emit()
        item = self.model.item(self.row, 0)
#         print "123", id(self.signalTime),repr(self.signalTime),type(self.signalTime),'att:',hasattr(self.signalTime,'emit')
#         print "********", self.signalTime.emit()
        if self.signalTime != None:
            effectTime = timedelta(microseconds = self.signalTime*1000)
        else:
            effectTime = timedelta(microseconds = 0)
        chooseField = ChooseField(self.sess, self.session,  item.text(), effectTime, self.musicSignal, self)
        acc = chooseField.exec_()
    
    def changedAliasNotes(self):
        item = self.model.item(self.row, 0)
        item1 = self.model.item(self.row, 4)
        item2 = self.model.item(self.row, 14)
        modifyAliasNotes = ModifyAliasNotes( self.sess, item.text(), item1.text(), item2.text(), self)
        accept = modifyAliasNotes.exec_()
        if accept == 1:
            self.model.clear()
            self.model.setHorizontalHeaderLabels (["UUID","Size (mm)", "Supplier", "Name", "Alias", "Rising Time", "Stock", "Weight Net", "Weight Gross", "Application", "Safety Distance Horizontal", "Safety Distance Vertical", "Information", "Price", "Notes"])
            self.query(self.Type)
            self.proxyView.hideColumn(0)
        
        
        
    def filterRegExpChanged(self):
        regExp = QRegExp(self.filterPatternLineEdit.text())
        self.proxyModel.setFilterRegExp(regExp)

    def filterColumnChanged(self):
        
        '''
        remarks: Because hidden a line so to plus one
        '''
        self.proxyModel.setFilterKeyColumn(self.filterColumnComboBox.currentIndex()+1)
        
        
    def filterBySize(self):
        if self.sizeComboBox.currentText() == "All" :
            regExp = QRegExp()
            self.proxyModel.setFilterRegExp(regExp)
            self.proxyModel.setFilterKeyColumn(1)
        else :
            regExp = QRegExp(str(float(self.sizeComboBox.currentText())*25.4))
            self.proxyModel.setFilterRegExp(regExp)
            self.proxyModel.setFilterKeyColumn(1)
#        pass
    
    def filterBySupplier(self):
        if self.supplierComboBox.currentText() == "All" :
            regExp = QRegExp()
            self.proxyModel.setFilterRegExp(regExp)
            self.proxyModel.setFilterKeyColumn(2)
        else :
            regExp = QRegExp(self.supplierComboBox.currentText())
            self.proxyModel.setFilterRegExp(regExp)
            self.proxyModel.setFilterKeyColumn(2)
#        pass

        
        





