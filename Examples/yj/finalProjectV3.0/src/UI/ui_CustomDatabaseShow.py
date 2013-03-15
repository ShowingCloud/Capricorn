from PySide import QtCore,QtGui
from ui_CustomDatabase import Ui_DatabaseDialog
from Models.LocalDB import *
import json, uuid
from datetime import timedelta, datetime

class uiCustomShow(QtGui.QDialog):
    def __init__(self, UUID, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_DatabaseDialog()
        self.ui.setupUi(self)
        
        self.sess = session()
        
        self.UUID = UUID
        self.getData(self.UUID)
        
        self.ui.pushButtonSave.clicked.connect(self.saveData)
        self.ui.pushButtonCancel.clicked.connect(self.cancel)
        
        self.ui.lineEditName.setReadOnly(True)
        self.ui.lineEdit_size.setReadOnly(True)
        self.ui.lineEdit_riseTime.setReadOnly(True)
        self.ui.lineEdit_shots.setReadOnly(True)
        self.ui.lineEdit_weightGross.setReadOnly(True)
        self.ui.lineEdit_weightNet.setReadOnly(True)
        self.ui.lineEdit_HorizSafeDistance.setReadOnly(True)
        self.ui.lineEdit_VertSafeDistance.setReadOnly(True)
        self.ui.lineEdit_riseHeight.setReadOnly(True)
        self.ui.lineEdit_diameter.setReadOnly(True)
        self.ui.lineEdit_Price.setReadOnly(True)
        self.ui.lineEdit_calcFactor.setReadOnly(True)
        
        
    def getData(self, UUID):
        with self.sess.begin():
            record = self.sess.query (FireworksData).filter_by(UUID = UUID).first()
            
            self.ui.lineEditName.setText(record.Name)
            self.ui.lineEditAlias.setText(record.Alias)
            self.ui.lineEdit_descript.setText(record.Description)
            self.ui.lineEdit_size.setText(str(record.Size))
            self.ui.lineEdit_usedEffect.setText(str(record.UsedEffects))
            self.ui.lineEdit_Min.setText(str(record.Min))
            self.ui.lineEdit_Best.setText(str(record.Best))
            self.ui.lineEdit_stock.setText(str(record.Stock))
            risTime = record.RisingTime
            self.ui.lineEdit_riseTime.setText(str(risTime.total_seconds()))
            info = json.loads(record.EffectsInfo)
            self.ui.lineEdit_effect1.setText(info["EffectsInfo"][0][0])
            self.ui.comboBoxColor1.setCurrentIndex(self.ui.comboBoxColor1.findText(info["EffectsInfo"][0][1]))
            self.ui.lineEdit_durationTime1.setText(str(info["EffectsInfo"][0][2]))
            
            self.ui.lineEdit_effect2.setText(info["EffectsInfo"][1][0])
            self.ui.comboBoxColor2.setCurrentIndex(self.ui.comboBoxColor2.findText(info["EffectsInfo"][1][1]))
            self.ui.lineEdit_durationTime2.setText(str(info["EffectsInfo"][1][2]))
            
            self.ui.lineEdit_effect3.setText(info["EffectsInfo"][2][0])
            self.ui.comboBoxColor3.setCurrentIndex(self.ui.comboBoxColor3.findText(info["EffectsInfo"][2][1]))
            self.ui.lineEdit_durationTime3.setText(str(info["EffectsInfo"][2][2]))
            
            self.ui.lineEdit_shots.setText(str(record.Shots))
            
            if record.Indoor == 0:
                self.ui.radioButton_indoor.isChecked()
            elif record.Indoor == 1:
                self.ui.radioButton_outdoor.isChecked()
            self.ui.lineEdit_riseHeight.setText(str(record.RisingHeight))
            self.ui.lineEdit_diameter.setText(str(record.Diameter))
            
            self.ui.lineEdit_class.setText(record.Class)
            self.ui.lineEdit_BAMnumber.setText(record.BAMNumber)
            self.ui.lineEdit_ADRclass.setText(record.ADRClass)
            self.ui.lineEdit_UNnumber.setText(record.UNNumber)
            self.ui.lineEdit_chiper.setText(str(record.Chipher))
            self.ui.lineEdit_weightGross.setText(str(record.WeightGross))
            self.ui.lineEdit_weightNet.setText(str(record.WeightNet))
            self.ui.lineEdit_HorizSafeDistance.setText(str(record.SDHorizontal))
            self.ui.lineEdit_VertSafeDistance.setText(str(record.SDVertical))
            self.ui.lineEdit_SimEffectID.setText(str(record.EffectID))
            self.ui.lineEdit_Rating.setText(record.Rating)
            
            self.ui.lineEdit_information.setText(record.Information)
            self.ui.lineEdit_supplier.setText(record.Supplier)
            self.ui.lineEdit_producer.setText(record.Producer)
            self.ui.lineEdit_itemNo.setText(record.ItemNo)
            self.ui.lineEdit_StockPlace.setText(record.StockPlace)
            self.ui.lineEdit_Price.setText(str(record.Price))
            self.ui.lineEdit_calcFactor.setText(str(record.CalcFactor))
            self.ui.textEditNotes.setText(record.Notes)
            
            
    def saveData(self):
        data = {"EffectsInfo" : [(self.ui.lineEdit_effect1.text(), self.ui.comboBoxColor1.currentText(), self.ui.lineEdit_durationTime1.text()), (self.ui.lineEdit_effect2.text(), self.ui.comboBoxColor2.currentText(), self.ui.lineEdit_durationTime2.text()),(self.ui.lineEdit_effect3.text(), self.ui.comboBoxColor3.currentText(), self.ui.lineEdit_durationTime3.text())]}
        d = json.dumps(data)
        
        with self.sess.begin():
            record = FireworksData()
            record.UUID = str(uuid.uuid1())
            record.CTime = datetime.utcnow()
            record.MTime = datetime.utcnow()
            record.Type = "Custom"
            record.Name = self.ui.lineEditName.text()
            record.Alias = self.ui.lineEditAlias.text()
            record.Description = self.ui.lineEdit_descript.text()
#            record.Picture = ""
#            record.Animation = ""
#            record.Model = ""
#            record.SoundEffect = ""
            
            record.Size = int(self.ui.lineEdit_size.text())
            record.UsedEffects = int(self.ui.lineEdit_usedEffect.text())
            record.Min = int(self.ui.lineEdit_Min.text())
            record.Best = int(self.ui.lineEdit_Best.text())
            record.Stock = int(self.ui.lineEdit_stock.text())
            record.RisingTime = timedelta(seconds = float(self.ui.lineEdit_riseTime.text()))
            record.EffectsInfo= d
            record.Shots = int(self.ui.lineEdit_shots.text())
            if self.ui.radioButton_indoor.isChecked():
                record.Indoor = 0
            if self.ui.radioButton_outdoor.isChecked():
                record.Indoor = 1
            record.RisingHeight = int(self.ui.lineEdit_riseHeight.text())
            record.Diameter = int(self.ui.lineEdit_diameter.text())
            record.Class = self.ui.lineEdit_class.text()
            record.BAMNumber = self.ui.lineEdit_BAMnumber.text()
            record.ADRClass = self.ui.lineEdit_ADRclass.text()
            record.UNNumber = self.ui.lineEdit_UNnumber.text()
            record.Chipher = int(self.ui.lineEdit_chiper.text())
            record.WeightGross = int(self.ui.lineEdit_weightGross.text())
            record.WeightNet = int(self.ui.lineEdit_weightNet.text())
            record.SDHorizontal = int(self.ui.lineEdit_HorizSafeDistance.text())
            record.SDVertical = int(self.ui.lineEdit_VertSafeDistance.text())
            record.EffectID = int(self.ui.lineEdit_SimEffectID.text())
            record.Rating = self.ui.lineEdit_Rating.text()
            record.Information = self.ui.lineEdit_information.text()
            record.Supplier = self.ui.lineEdit_supplier.text()
            record.Producer = self.ui.lineEdit_producer.text()
            record.ItemNo = self.ui.lineEdit_itemNo.text()
            record.StockPlace = self.ui.lineEdit_StockPlace.text()
            record.Price = int(self.ui.lineEdit_Price.text())
            record.CalcFactor = int(self.ui.lineEdit_calcFactor.text())
            record.Notes = self.ui.textEditNotes.toPlainText()
            record.Perm = 0        #
#            record.Owner = ""         
#
            self.sess.add(record)

        
        self.accept()
        self.close()
            
        
        
        
    def cancel(self):
        self.close()
        
 
