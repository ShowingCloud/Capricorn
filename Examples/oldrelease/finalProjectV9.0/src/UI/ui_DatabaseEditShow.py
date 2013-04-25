from Models.LocalDB import *
from PySide import QtGui, QtCore
from PySide.QtCore import Slot
from datetime import datetime, timedelta
from ui_DatabaseEdit import Ui_DatabaseDialog
import json
import uuid

class  uiShow(QtGui.QDialog):
    def __init__(self, sess, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_DatabaseDialog()
        self.ui.setupUi(self)
        
        self.ui.pushButtonSave.clicked.connect(self.saveData)
        self.ui.pushButtonCancel.clicked.connect(self.cancel)
        
        self.ui.comboBoxColor1.currentIndexChanged.connect(self.changeColor1)
        self.ui.comboBoxColor2.currentIndexChanged.connect(self.changeColor2)
        self.ui.comboBoxColor3.currentIndexChanged.connect(self.changeColor3)
        self.sess = sess
        
        
    def saveData(self):
        data = {"EffectsInfo" : [(self.ui.lineEdit_effect1.text(), self.ui.comboBoxColor1.currentText(), self.ui.lineEdit_durationTime1.text()), (self.ui.lineEdit_effect2.text(), self.ui.comboBoxColor2.currentText(), self.ui.lineEdit_durationTime2.text()),(self.ui.lineEdit_effect3.text(), self.ui.comboBoxColor3.currentText(), self.ui.lineEdit_durationTime3.text())]}
        d = json.dumps(data)
        
        with self.sess.begin():
            record = FireworksData()
            record.UUID = str(uuid.uuid1())
            record.CTime = datetime.utcnow()
            record.MTime = datetime.utcnow()
            record.Type = self.ui.comboBoxType.currentText()
            record.Name = self.ui.lineEditName.text()
            record.Alias = self.ui.lineEditAlias.text()
            record.Description = self.ui.lineEdit_descript.text()
#            record.Picture = ""
#            record.Animation = ""
#            record.Model = ""
#            record.SoundEffect = ""
            
            record.Size = self.ui.lineEdit_size.text()
            record.UsedEffects = self.ui.lineEdit_usedEffect.text()
            record.Min = self.ui.lineEdit_Min.text()
            record.Best = self.ui.lineEdit_Best.text()
            record.Stock = self.ui.lineEdit_stock.text()
            record.RisingTime = timedelta(seconds = float(self.ui.lineEdit_riseTime.text()))
            record.EffectsInfo= d
            record.Shots = self.ui.lineEdit_shots.text()
            if self.ui.radioButton_indoor.isChecked():
                record.Indoor = 0
            if self.ui.radioButton_outdoor.isChecked():
                record.Indoor = 1
            record.RisingHeight = self.ui.lineEdit_riseHeight.text()
            record.Diameter = self.ui.lineEdit_diameter.text()
            record.Class = self.ui.lineEdit_class.text()
            record.BAMNumber = self.ui.lineEdit_BAMnumber.text()
            record.ADRClass = self.ui.lineEdit_ADRclass.text()
            record.UNNumber = self.ui.lineEdit_UNnumber.text()
            record.Chipher = self.ui.lineEdit_chiper.text()
            record.WeightGross = self.ui.lineEdit_weightGross.text()
            record.WeightNet = self.ui.lineEdit_weightNet.text()
            record.SDHorizontal = self.ui.lineEdit_HorizSafeDistance.text()
            record.SDVertical = self.ui.lineEdit_VertSafeDistance.text()
            record.EffectID = self.ui.lineEdit_SimEffectID.text()
            record.Rating = self.ui.lineEdit_Rating.text()
            record.Information = self.ui.lineEdit_information.text()
            record.Supplier = self.ui.lineEdit_supplier.text()
            record.Producer = self.ui.lineEdit_producer.text()
            record.ItemNo = self.ui.lineEdit_itemNo.text()
            record.StockPlace = self.ui.lineEdit_StockPlace.text()
            record.Price = self.ui.lineEdit_Price.text()
            record.CalcFactor = self.ui.lineEdit_calcFactor.text()
            record.Notes = self.ui.textEditNotes.toPlainText()
            record.Perm = 1        #
#            record.Owner = ""         
#
            self.sess.add(record)

        
        self.accept()
        self.close()
        
        
    def cancel(self):
        self.close()
        
    
    @Slot(int)   
    def changeColor1(self, index):
        self.ui.IconLabel_color1.setAutoFillBackground(True)
        if index == 0:
            self.ui.IconLabel_color1.setStyleSheet("QLabel{background-color: transparent}")
        else :
            self.ui.IconLabel_color1.setStyleSheet("QLabel{background-color:%s}" % self.ui.comboBoxColor1.itemText(index))
            
            
    @Slot(int)   
    def changeColor2(self, index):
        self.ui.IconLabel_color2.setAutoFillBackground(True)
        if index == 0:
            self.ui.IconLabel_color2.setStyleSheet("QLabel{background-color: transparent}")
        else :
            self.ui.IconLabel_color2.setStyleSheet("QLabel{background-color:%s}" % self.ui.comboBoxColor2.itemText(index))
            
    @Slot(int)   
    def changeColor3(self, index):
        self.ui.IconLabel_color3.setAutoFillBackground(True)
        if index == 0:
            self.ui.IconLabel_color3.setStyleSheet("QLabel{background-color: transparent}")
        else :
            self.ui.IconLabel_color3.setStyleSheet("QLabel{background-color:%s}" % self.ui.comboBoxColor3.itemText(index))
 
