#!/usr/bin/python

import sys

from PySide import QtCore, QtGui

from sqlalchemy import Column, Integer, Sequence, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from datetime import datetime


engine = create_engine ('sqlite:///test.db')
session = scoped_session (sessionmaker (bind = engine, autocommit = True))
base = declarative_base()


class Data (base):
	__tablename__ = 'Data'

	id = Column (Integer, Sequence ('session_id_seq'), primary_key = True)
	info = Column (String)
	time = Column (DateTime)

	def __init__ (self, info = None, time = None):
		self.info = info
		self.time = time

	def __repr__ (self):
		return self.info


class TestSQL (QtGui.QWidget):

	def __init__ (self):
		QtGui.QWidget.__init__ (self)
		self.setWindowTitle ("TestSQL")

		self.edit = QtGui.QLineEdit (self)
		self.buttonFirst = QtGui.QPushButton ("Show First", self)
		self.buttonNext = QtGui.QPushButton ("Show Next", self)
		self.buttonInsert = QtGui.QPushButton ("Insert", self)

		layout = QtGui.QGridLayout (self)
		layout.addWidget (self.edit, 0, 0, 1, 3)
		layout.addWidget (self.buttonFirst, 1, 0)
		layout.addWidget (self.buttonNext, 1, 1)
		layout.addWidget (self.buttonInsert, 1, 2)

		self.buttonFirst.clicked.connect (self.showfirst)
		self.buttonNext.clicked.connect (self.shownext)
		self.buttonInsert.clicked.connect (self.insert)

		base.metadata.create_all (engine)
		self.sess = session()
		self.shownum = 0

	def showfirst (self):
		with self.sess.begin():
			q = self.sess.query (Data)

			if q.count() == 0:
				self.edit.setText ("No data in the database")
				self.shownum = 0
			else:
				record = q.first()
				self.edit.setText (record.__repr__())
				self.shownum = 1

	def shownext (self):
		with self.sess.begin():
			q = self.sess.query (Data)

			if q.count() == 0:
				self.edit.setText ("No data in the database")
				self.shownum = 0
			elif self.shownum < q.count():
				record = q.all()[self.shownum]
				self.edit.setText (record.__repr__())
				self.shownum += 1
			else:
				record = q.all()[0]
				self.edit.setText (record.__repr__())
				self.shownum = 0

	def insert (self):
		with self.sess.begin():
			record = Data()
			record.info = self.edit.text()
			record.time = datetime.now()
			# or
			# record = Data (info = self.edit.text(), time = datetime.now())

			self.sess.add (record)


if __name__ == "__main__":
	app = QtGui.QApplication (sys.argv)
	app.setApplicationName ("TestSQL")
	window = TestSQL()
	window.show()
	sys.exit (app.exec_())
