#!/usr/bin/python

import wave, struct

class waveform():

	def __init__ (self):
		self.audio = wave.open ('Rossini.wav', 'r')

	def read (self, size):
		data = self.audio.readframes (size)

		sw = self.audio.getsampwidth()
		data = struct.unpack ('<%d%s' % (len (data) / sw,
			wave._array_fmts[sw]), data)

		nc = self.audio.getnchannels()
		if nc > 1:
			left = [data[si] for si in xrange (0, len (data), nc)]
			right = [data[si] for si in xrange (1, len (data), nc)]
			sample = []
			sample.append (left)
			sample.append (right)
		else:
			sample = data

		return sample

	def waveform (self):
		print self.read (self.audio.getnframes())
              
if __name__ == "__main__":
	waveform = waveform()
	waveform.waveform()
