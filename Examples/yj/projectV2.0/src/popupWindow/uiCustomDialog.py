#coding=utf-8
'''
Created on 2013-2-20

@author: pyroshow

'''

import sys
from PySide.QtGui import *
from PySide.QtCore import *
from alchemy.AlchemyOpereation import *


class CustomDialog(QDialog):
    
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.TypeLabel = QLabel("Type:")
        self.ItemLabel = QLabel("Item:")
        self.DescriptionLabel = QLabel("Description:")
        self.SizeLabel = QLabel("Size:")
        self.StockLabel = QLabel("Stock:")
        self.UsedEffectsLabel = QLabel("Used Effects:")
        self.RisingTimeLabel = QLabel("Rising Time:")
        self.EffectLabel = QLabel("Effect:")
        self.ColorLabel = QLabel("Color:")
        self.AngleLabel = QLabel("Angle:")

        self.TypeEdit = QComboBox()
        self.TypeEdit.addItems(['A', 'B', 'C', 'D', 'Combination'])
        self.ItemEdit = QLineEdit()
        self.DescriptionEdit = QLineEdit()
        
        self.SizeEdit = QLineEdit()
        aIntValidator = QIntValidator()
        self.SizeEdit.setValidator(aIntValidator)
        
        self.StockEdit = QLineEdit()
        aIntValidator = QIntValidator()
        self.StockEdit.setValidator(aIntValidator)
        
        self.UsedEffectsEdit = QLineEdit()
        aIntValidator = QIntValidator()
        self.UsedEffectsEdit.setValidator(aIntValidator)
        
        self.RisingTimeEdit = QLineEdit()
        aDoubleValidator = QDoubleValidator()
        self.RisingTimeEdit.setValidator(aDoubleValidator)
        
        self.EffectEdit = QLineEdit()
        
        self.ColorEdit = QComboBox()
        self.ColorEdit.addItems(['transparent', 'white', 'black', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'gray', 'lightGray'])
        
        self.AngleEdit = QComboBox()
        self.AngleEdit.addItems(['0', '30', '45', '60', '90', '120', '135', '150', '180'])
        
        self.saveButton = QPushButton("Save")
        self.cancelButton = QPushButton("Cancel")
        
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.TypeLabel, 0, 0)
        self.layout.addWidget(self.TypeEdit, 0, 1)
        self.layout.addWidget(self.ItemLabel, 0, 2)
        self.layout.addWidget(self.ItemEdit, 0, 3)
        self.layout.addWidget(self.DescriptionLabel, 1, 0)
        self.layout.addWidget(self.DescriptionEdit, 1, 1)
        self.layout.addWidget(self.SizeLabel, 1, 2)
        self.layout.addWidget(self.SizeEdit, 1, 3)
        self.layout.addWidget(self.StockLabel, 2, 0)
        self.layout.addWidget(self.StockEdit, 2, 1)
        self.layout.addWidget(self.UsedEffectsLabel, 2, 2)
        self.layout.addWidget(self.UsedEffectsEdit, 2, 3)
        self.layout.addWidget(self.RisingTimeLabel, 3, 0)
        self.layout.addWidget(self.RisingTimeEdit, 3, 1)
        self.layout.addWidget(self.EffectLabel, 3, 2)
        self.layout.addWidget(self.EffectEdit, 3, 3)
        self.layout.addWidget(self.ColorLabel, 4, 0)
        self.layout.addWidget(self.ColorEdit, 4, 1)
        self.layout.addWidget(self.AngleLabel, 4, 2)
        self.layout.addWidget(self.AngleEdit, 4, 3)
        self.layout.addWidget(self.saveButton, 5, 0, 1, 2)
        self.layout.addWidget(self.cancelButton, 5, 2, 1, 2)
        self.setLayout(self.layout)
        
        self.saveButton.clicked.connect(self.saveData)
        self.cancelButton.clicked.connect(self.cancel)
        
        self.sess = session()
        
        
    def saveData(self):
        with self.sess.begin():
            record = Data1()
            record.Type = self.TypeEdit.currentText()
            record.Item = self.ItemEdit.text()
            record.Description = self.DescriptionEdit.text()
            record.Size = self.SizeEdit.text()
            record.Stock = self.StockEdit.text()
            record.Used_Effects = self.UsedEffectsEdit.text()
            record.Rising_Time = self.RisingTimeEdit.text()
            record.Effect = self.EffectEdit.text()
            record.Color = self.ColorEdit.currentText()
            record.Angle = self.AngleEdit.currentText()

            self.sess.add(record)

        self.TypeEdit.setCurrentIndex(0)
        self.ItemEdit.setText("")
        self.SizeEdit.setText("")
        self.DescriptionEdit.setText("")
        self.StockEdit.setText("")
        self.UsedEffectsEdit.setText("")
        self.RisingTimeEdit.setText("")
        self.EffectEdit.setText("")
        self.ColorEdit.setCurrentIndex(0)
        self.AngleEdit.setCurrentIndex(0)
        
        self.accept()
        
        
    def cancel(self):
        self.close()