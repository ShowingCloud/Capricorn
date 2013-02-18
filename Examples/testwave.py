#!/usr/bin/python

import wave, struct

class waveform():

	def __init__ (self):
		self.audio = wave.open ('test.wav', 'r')
		self.nchannels, self.sampwidth, self.framerate, self.nframes, self.comptype, self.compname = self.audio.getparams()
                
	def read (self, size):
		self.audio.setpos (0)
		data = self.audio.readframes (size)

		if self.sampwidth == 1:
			packstr = '%sb'
		elif self.sampwidth == 2:
			packstr = '%sh'
		elif self.sampwidth == 4:
			packstr = '%si'
		elif self.sampwidth == 8:
			packstr = '%sq'
		else:
			return None

		if self.nchannels == 1:
			sample = struct.unpack (packstr % size, data)
		else:
			sample = []
			left = data[:, 0]
			sample.append (struct.unpack (packstr % size, left))
			right = data[:, 1]
			sample.append (struct.unpack (packstr % size, right))

		return sample

	def waveform (self):
		print self.read (self.nframes)
              
if __name__ == "__main__":
	waveform = waveform()
	waveform.waveform()
