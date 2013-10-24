from Models.LocalDB import FireworksData
from PySide import QtGui
from PySide.QtCore import Slot
from datetime import datetime
from UI.ui_editFireworks import Ui_DatabaseDialog
import json
import uuid

class  EditFireworks(QtGui.QDialog):
    def __init__(self, localSession, editUUID = None, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_DatabaseDialog()
        self.ui.setupUi(self)
        self.ui.pushButtonSave.clicked.connect(self.saveData)
        self.ui.pushButtonCancel.clicked.connect(self.cancel)
        
        self.ui.comboBoxColor1.currentIndexChanged.connect(self.changeColor1)
        self.ui.comboBoxColor2.currentIndexChanged.connect(self.changeColor2)
        self.ui.comboBoxColor3.currentIndexChanged.connect(self.changeColor3)
        self.localSession = localSession
        self.parent = parent
        self.editUUID = editUUID
        
        if self.editUUID != None :
            self.ui.pushButtonSave.setText("Update")
            self.load()
        
        
    def load(self):
        
        with self.localSession.begin():
            fireworksRecord = self.localSession.query(FireworksData).filter_by(UUID = self.editUUID).first()
        effectInfo = json.loads(fireworksRecord.EffectsInfo)
        self.ui.comboBoxType.setCurrentIndex(self.ui.comboBoxType.findText(fireworksRecord.Type))
        self.ui.lineEditName.setText(fireworksRecord.Name)
        self.ui.lineEditAlias.setText(fireworksRecord.Alias)
        self.ui.lineEdit_descript.setText(fireworksRecord.Description)
        self.ui.lineEdit_size.setText(str(fireworksRecord.Size))
        self.ui.lineEdit_usedEffect.setText(str(fireworksRecord.UsedEffects))
        
        
        self.ui.lineEdit_Min.setText(str(fireworksRecord.Min))
        self.ui.lineEdit_Best.setText(str(fireworksRecord.Best))
        self.ui.lineEdit_stock.setText(str(fireworksRecord.Stock))
        
        self.ui.lineEdit_riseTime.setText(str((fireworksRecord.RisingTime / 1000.0)))
        
        self.ui.lineEdit_effect1.setText(effectInfo["EffectsInfo"][0][0])
        self.ui.comboBoxColor1.setCurrentIndex(self.ui.comboBoxColor1.findText(effectInfo["EffectsInfo"][0][1]))
        self.ui.lineEdit_durationTime1.setText(effectInfo["EffectsInfo"][0][2])
        
        self.ui.lineEdit_effect2.setText(effectInfo["EffectsInfo"][1][0])
        self.ui.comboBoxColor2.setCurrentIndex(self.ui.comboBoxColor2.findText(effectInfo["EffectsInfo"][1][1]))
        self.ui.lineEdit_durationTime2.setText(effectInfo["EffectsInfo"][1][2])
        
        self.ui.lineEdit_effect3.setText(effectInfo["EffectsInfo"][2][0])
        self.ui.comboBoxColor3.setCurrentIndex(self.ui.comboBoxColor3.findText(effectInfo["EffectsInfo"][2][1]))
        self.ui.lineEdit_durationTime3.setText(effectInfo["EffectsInfo"][2][2])
        
        self.ui.lineEdit_shots.setText(str(fireworksRecord.Shots))
        if fireworksRecord.Indoor == 0:
            self.ui.radioButton_indoor.isChecked()
        else:
            self.ui.radioButton_outdoor.isChecked()
        self.ui.lineEdit_riseHeight.setText(str(fireworksRecord.RisingHeight))
        
        self.ui.lineEdit_diameter.setText(str(fireworksRecord.Diameter))
        self.ui.lineEdit_class.setText(fireworksRecord.Class)
        self.ui.lineEdit_BAMnumber.setText(fireworksRecord.BAMNumber)
        self.ui.lineEdit_ADRclass.setText(fireworksRecord.ADRClass)
        self.ui.lineEdit_UNnumber.setText(fireworksRecord.UNNumber)
        self.ui.lineEdit_chiper.setText(str(fireworksRecord.Chipher))
        self.ui.lineEdit_weightGross.setText(str(fireworksRecord.WeightGross))
        self.ui.lineEdit_weightNet.setText(str(fireworksRecord.WeightNet))
        self.ui.lineEdit_HorizSafeDistance.setText(str(fireworksRecord.SDHorizontal))
        
        self.ui.lineEdit_VertSafeDistance.setText(str(fireworksRecord.SDVertical))
        self.ui.lineEdit_SimEffectID.setText(fireworksRecord.EffectID)
        self.ui.lineEdit_Rating.setText(fireworksRecord.Rating)
        self.ui.lineEdit_information.setText(fireworksRecord.Information)
        self.ui.lineEdit_supplier.setText(fireworksRecord.Supplier)
        self.ui.lineEdit_producer.setText(fireworksRecord.Producer)
        
        self.ui.lineEdit_itemNo.setText(fireworksRecord.ItemNo)
        self.ui.lineEdit_StockPlace.setText(fireworksRecord.StockPlace)
        self.ui.lineEdit_Price.setText(str(fireworksRecord.Price))
        self.ui.lineEdit_calcFactor.setText(str(fireworksRecord.CalcFactor))
        self.ui.textEditNotes.setText(fireworksRecord.Notes)
        
        
    def saveData(self):
        data = {"EffectsInfo" : [(self.ui.lineEdit_effect1.text(), self.ui.comboBoxColor1.currentText(), self.ui.lineEdit_durationTime1.text()), (self.ui.lineEdit_effect2.text(), self.ui.comboBoxColor2.currentText(), self.ui.lineEdit_durationTime2.text()),(self.ui.lineEdit_effect3.text(), self.ui.comboBoxColor3.currentText(), self.ui.lineEdit_durationTime3.text())]}
        d = json.dumps(data)
        if self.editUUID == None :
            with self.localSession.begin():
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
                record.RisingTime = int(float(self.ui.lineEdit_riseTime.text())*1000)
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
                self.localSession.add(record)
                
        else :
            with self.localSession.begin():
                record =  self.localSession.query(FireworksData).filter_by(UUID = self.editUUID).first()
            
                record.Type = self.ui.comboBoxType.currentText()
                record.Name = self.ui.lineEditName.text()
                record.Alias = self.ui.lineEditAlias.text()
                record.Description = self.ui.lineEdit_descript.text()
                
                record.Size = self.ui.lineEdit_size.text()
                record.UsedEffects = self.ui.lineEdit_usedEffect.text()
                record.Min = self.ui.lineEdit_Min.text()
                record.Best = self.ui.lineEdit_Best.text()
                record.Stock = self.ui.lineEdit_stock.text()
                record.RisingTime = int(float(self.ui.lineEdit_riseTime.text())*1000)
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
            
        self.accept()
        
        
    def cancel(self):
        self.close()
        
    def getMessage(self,dicKey):
        dicEnglish = {}
        dicEnglish.setdefault(str(self.tr('White')), 'White')
        dicEnglish.setdefault(str(self.tr('Black')), 'Black')
        dicEnglish.setdefault(str(self.tr('Red')), 'Red')
        dicEnglish.setdefault(str(self.tr('Blue')), 'Blue')
        dicEnglish.setdefault(str(self.tr('Green')), 'Green')
        dicEnglish.setdefault(str(self.tr('Cyan')), 'Cyan')
        dicEnglish.setdefault(str(self.tr('Magenta')), 'Magenta')
        dicEnglish.setdefault(str(self.tr('Yellow')), 'Yellow')
        dicEnglish.setdefault(str(self.tr('Gray')), 'Gray') 
        return dicEnglish[str(dicKey)]
    
    @Slot(int)   
    def changeColor1(self, index):
        self.ui.IconLabel_color1.setAutoFillBackground(True)
        if index == 0:
            self.ui.IconLabel_color1.setStyleSheet("QLabel{background-color: transparent}")
        else :
            self.ui.IconLabel_color1.setStyleSheet("QLabel{background-color:%s}" % self.getMessage(self.ui.comboBoxColor1.itemText(index)))
            
            
    @Slot(int)   
    def changeColor2(self, index):
        self.ui.IconLabel_color2.setAutoFillBackground(True)
        if index == 0:
            self.ui.IconLabel_color2.setStyleSheet("QLabel{background-color: transparent}")
        else :
            self.ui.IconLabel_color2.setStyleSheet("QLabel{background-color:%s}" % self.getMessage(self.ui.comboBoxColor2.itemText(index)))
            
    @Slot(int)   
    def changeColor3(self, index):
        self.ui.IconLabel_color3.setAutoFillBackground(True)
        if index == 0:
            self.ui.IconLabel_color3.setStyleSheet("QLabel{background-color: transparent}")
        else :
            self.ui.IconLabel_color3.setStyleSheet("QLabel{background-color:%s}" % self.getMessage(self.ui.comboBoxColor3.itemText(index)))
 
