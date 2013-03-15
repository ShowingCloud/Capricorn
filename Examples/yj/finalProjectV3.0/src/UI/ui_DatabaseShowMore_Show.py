from PySide import QtCore,QtGui
from ui_DatabaseShowMore import Ui_DatabaseDialog
from Models.LocalDB import *
import json
from datetime import timedelta

class uiShowMore(QtGui.QDialog):
    def __init__(self, UUID, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_DatabaseDialog()
        self.ui.setupUi(self)
        
        self.sess = session()
        
        self.UUID = UUID
        self.getData(self.UUID)
        
        
    def getData(self, UUID):
        with self.sess.begin():
            record = self.sess.query (FireworksData).filter_by(UUID = UUID).first()
            
            self.ui.comboBoxType.setCurrentIndex(self.ui.comboBoxType.findText(record.Type))
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
                self.ui.radioButton_indoor.setChecked(True)
                self.ui.radioButton_outdoor.setChecked(False)
            elif record.Indoor == 1:
                self.ui.radioButton_indoor.setChecked(False)
                self.ui.radioButton_outdoor.setChecked(True)
                
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
            
        
        
        
    def cancel(self):
        self.close()
        
 
