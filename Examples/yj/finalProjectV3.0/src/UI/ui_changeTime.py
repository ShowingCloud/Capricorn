#coding=utf-8
'''
Created on 2013-3-15

@author: pyroshow
'''
from PySide import QtGui, QtCore
import sys

class ChangeTime(QtGui.QDialog):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        
        self.groupBox = QtGui.QGroupBox("Change time:")
        
        self.ignitionLable = QtGui.QLabel("Ignition Time:")
        self.hourBox_i = QtGui.QSpinBox()
        self.label_h_i = QtGui.QLabel(":")
        self.minuteBox_i = QtGui.QSpinBox()
        self.label_m_i = QtGui.QLabel(":")
        self.secondBox_i = QtGui.QSpinBox()
        self.label_s_i = QtGui.QLabel(".")
        self.microBox_i = QtGui.QSpinBox()
        
        self.EffectLable = QtGui.QLabel("Effect Time:")
        self.hourBox_e = QtGui.QSpinBox()
        self.label_h_e = QtGui.QLabel(":")
        self.minuteBox_e = QtGui.QSpinBox()
        self.label_m_e = QtGui.QLabel(":")
        self.secondBox_e = QtGui.QSpinBox()
        self.label_s_e = QtGui.QLabel(".")
        self.microBox_e = QtGui.QSpinBox()
        
        grid = QtGui.QGridLayout()
        
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(self.hourBox_i)
        hbox1.addWidget(self.label_h_i)
        hbox1.addWidget(self.minuteBox_i)
        hbox1.addWidget(self.label_m_i)
        hbox1.addWidget(self.secondBox_i)
        hbox1.addWidget(self.label_s_i)
        hbox1.addWidget(self.microBox_i)
        
        
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.hourBox_e)
        hbox2.addWidget(self.label_h_e)
        hbox2.addWidget(self.minuteBox_e)
        hbox2.addWidget(self.label_m_e)
        hbox2.addWidget(self.secondBox_e)
        hbox2.addWidget(self.label_s_e)
        hbox2.addWidget(self.microBox_e)
        grid.addWidget(self.ignitionLable, 0, 0)
        grid.addWidget(self.EffectLable, 0, 3)
        
        grid.addLayout( hbox1, 1, 0,1, 2)
        grid.addLayout(hbox2, 1, 3, 1, 2)
        
        self.groupBox.setLayout(grid)
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        
        self.setLayout(mainLayout)
        
app = QtGui.QApplication(sys.argv)

demo = ChangeTime()
demo.show()
sys.exit(app.exec_())




