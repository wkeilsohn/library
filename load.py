import pandas as pd
from internal.models import *
from internal import app, db

path = '~/Documents/Python_Scripts/oasis_library/virtual/Add_Data/'

files = {'st': 'state.csv', 'hc': 'CVS_codes.csv', 'bk': 'Library_Master.csv'}


def addState():
	s = path + files['st']
	df = pd.read_csv(s)
	ms = 0
	for index, row in df.iterrows():
		try:
			s = State(State=row['State'], Abbreviation=row['Code'])
			db.session.add(s)
			db.session.commit()
		except:
			ms = ms + 1
	print(str(ms) + ' States failed to load.')


def addType():
	h = path + files['hc']
	df = pd.read_csv(h)
	mh = 0
	for index, row in df.iterrows():
		try:
			h = Holiday(Name=row[1], Code=row[0])
			db.session.add(h)
			db.session.commit()
		except:
			mh = mh + 1
	print(str(mh) + ' Holidays failed to load.')


def addAuthor(df):
	print('Authors failed to load.')

def addPublisher(df):
	print('Publishers failed to load.')


def bookLoader():
	dp = path + files['bk']
	df = pd.read_csv(dp)
