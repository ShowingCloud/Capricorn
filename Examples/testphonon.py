#!/usr/bin/python

import sys

from PySide import QtCore, QtGui
from PySide.phonon import Phonon

class Window (QtGui.QWidget):

	def __init__ (self):
		QtGui.QWidget.__init__ (self)
		self.setWindowTitle ('Player')

		self.media = Phonon.MediaObject (self)
		self.media.setCurrentSource (Phonon.MediaSource ("test.wav"))
		self.media.finished.connect (app.quit)

		self.output = Phonon.AudioOutput (self)
		Phonon.createPath (self.media, self.output)

		self.buttonPlay = QtGui.QPushButton ('Play', self)
		self.buttonPause = QtGui.QPushButton ('Pause', self)
		self.slider = Phonon.VolumeSlider (self)
		self.slider.setAudioOutput (self.output)

		layout = QtGui.QGridLayout (self)
		layout.addWidget (self.buttonPlay, 0, 0)
		layout.addWidget (self.buttonPause, 0, 1)
		layout.addWidget (self.slider, 1, 0, 1, 2)
		layout.setRowStretch (0, 1)

		self.media.stateChanged.connect (self.stateChanged)
		self.buttonPlay.clicked.connect (self.changePlayStop)
		self.buttonPause.clicked.connect (self.changePauseResume)

	def changePlayStop (self):
		if self.media.state() == Phonon.PlayingState:
			self.media.stop()
		else:
			self.media.play()

	def changePauseResume (self):
		self.media.pause()
		# TODO: resume

	def stateChanged (self, newstate, oldstate):
		if newstate == Phonon.PlayingState:
			self.buttonPlay.setText ('Stop')
		elif (newstate != Phonon.LoadingState and
				newstate != Phonon.BufferingState):
			self.buttonPlay.setText ('Play')
			if newstate == Phonon.ErrorState:
				print ('ERROR: could not play: %s' % self.media.errorString())

if __name__ == "__main__":

	app = QtGui.QApplication (sys.argv)
	app.setApplicationName ("Player")
	window = Window()
	window.show()
	sys.exit (app.exec_())
