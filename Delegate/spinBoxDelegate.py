#coding=utf-8
'''
Created on 2013-10-12

@author: YuJin
'''
from PySide import QtGui, QtCore
from Models.ProjectDB import ProFireworksData

class SpinBoxDelegate(QtGui.QStyledItemDelegate):

    def __init__(self, proSession, parent = None):
        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.parent = parent
        self.proSession = proSession
        
#    #重写自带方法(参数自带)
    def paint(self, painter, option, index):
         
        style = QtGui.QApplication.style()
        label = QtGui.QStyleOptionViewItemV4 (option)
        label.text = str(index.data())
        label.displayAlignment = QtCore.Qt.AlignCenter
        
        style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)

    def createEditor (self, parent, option, index):
        
        spinBox = QtGui.QSpinBox(parent)
        spinBox.setMinimum(1)
        spinBox.setMaximum(999)
        spinBox.installEventFilter(self)
        return spinBox
    
    def setEditorData(self, editor, index):
        editor.setValue(index.data())
            
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
        
    def setModelData(self, editor, model, index):
        
        #统计相同点火盒的烟花
        sumBoxID = [row for row in self.parent.scriptTable if row.IgnitorID == editor.value()]
        if  (16 - len(sumBoxID)) < 1 :
            msgBox = QtGui.QMessageBox(self.parent)
            msgBox.setText("SurplusHeads not enough!!!\n Please choose other Ignition Box!")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
            return
#         data = editor.value()
#         model.setData(index, data)
        
        scriptUUID = self.parent.proModel.item(index.row(), 0).text()
        with self.proSession.begin():
            scriptData = self.proSession.query(ProFireworksData).filter_by(UUID = scriptUUID).first()
            scriptData.IgnitorID = editor.value() 
            scriptData.ConnectorID = self.distributionIgnitor(editor.value())
        self.parent.refreshScript()
    
    #自动分配点火盒，
    def distributionIgnitor(self, boxID):
        ConnectorID = 0
        tempData = 1
        for i in xrange(tempData, 17):
            if len([row for row in self.parent.scriptTable if row.IgnitorID == boxID and row.ConnectorID == i]) == 0:
                ConnectorID = i
                tempData += 1
                break
        return ConnectorID
        
