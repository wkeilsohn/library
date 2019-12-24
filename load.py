import pandas as pd
from internal.models import *
from internal import app, db

path = '~/Documents/Python_Scripts/oasis_library/virtual/Add_Data/'

def addStates():
	s = path + 'state.csv'
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