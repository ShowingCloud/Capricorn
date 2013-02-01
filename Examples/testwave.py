#!/usr/bin/python

import wave, struct

class waveform():

	def __init__ (self):
		self.audio = wave.open ('test.wav', 'r')
		self.nchannels, self.sampwidth, self.framerate, self.nframes, self.comptype, self.compname = self.audio.getparams()
                
	def cell (self, start, size, channel):
		self.audio.setpos (start)
		data = self.audio.readframes (size)

		if channel != -1:
			data = data[:, channel] # take one of the channels

		if self.sampwidth == 1:
			sample = struct.unpack ('%sb' % size, data)
		elif self.sampwidth == 2:
			sample = struct.unpack ('%sh' % size, data)
		elif self.sampwidth == 4:
			sample = struct.unpack ('%si' % size, data)
		elif self.sampwidth == 8:
			sample = struct.unpack ('%sq' % size, data)

		return (min (sample), max (sample))

	def read (self, starttime, endtime, number):
		start = starttime * self.framerate / 1000 # both starttime and endtime are millisecondes, e.g.
		end = endtime * self.framerate / 1000
		interval = (end - start) / number

		for i in xrange (number):
			if self.nchannels > 1: # if we've got several channels, take the first two
				print self.cell (start + i * interval, interval, 0)
				print self.cell (start + i * interval, interval, 1)
			else:
				print self.cell (start + i * interval, interval, -1)

	def waveform (self):
		self.read (0, 1000, 100) # from 0s to 1s, with 100 grids
              
if __name__ == "__main__":
	waveform = waveform()
	waveform.waveform()
