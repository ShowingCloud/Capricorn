#!/usr/bin/python

import wave, numpy

class waveform():

	def __init__ (self):
		self.audio = wave.open ('Rossini.wav', 'r')

	def read (self, size):
		data = self.audio.readframes (size)

		sw = self.audio.getsampwidth()
		data = numpy.frombuffer (data, dtype = numpy.dtype ("i%d" % sw))

		nc = self.audio.getnchannels()
		if nc > 1:
			left = data[0::nc]
			right = data[1::nc]
			sample = [left, right]
		else:
			sample = data

		return sample

	def waveform (self):
		wav = self.read (self.audio.getnframes())

if __name__ == "__main__":
	waveform = waveform()
	waveform.waveform()
