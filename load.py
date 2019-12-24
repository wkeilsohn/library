import pandas as pd
from internal.models import *
from internal import app, db
import re

path = '~/Documents/Python_Scripts/oasis_library/virtual/Add_Data/'

files = {'st': 'state.csv', 'hc': 'CVS_codes.csv', 'bk': 'Library_Master.csv'}

ch = 50 # Chunk size subject to change.

cates = ['With_Plans', 'ABC_Count', 'Award', 'Begining_Reading', 'BegRd_ChapterBk', 'Biography', 'Mystery',\
'Fables_Folktales', 'Game', 'Paired', 'Poetry_Ridd_Codes', 'Professional', 'Science', \
'Shared_Rd', 'Sports', 'Wordless', 'Holiday_Seasons']


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


def addAuthor(ls):
	ma = 0
	for i in ls:
		name = re.split(', |. |& |.', i)
		try:
			lm = name[0]
			fm = name[1]
			if i.find('&') > -1 and len(name) > 4:
				if len(name[2]) == 1:
					mm = name[2]
				else:
					mm = ''
			elif len(name) == 3 and i.find('&') == -1:
				mm = name[2]
			else:
				mm = ''
			a = Author(FirstName=fm, MiddleName=mm, LastName=lm)
			db.session.add(a)
			db.session.commit()
		except:
			ma = ma +1
	print(str(ma) + ' Authors failed to load.')

'''
### No Publishers provided in sample data. ### 

def addPublisher(df):
	print('Publishers failed to load.')
'''

def addType(df):
	mt = 0
	t = []
	for index, row in df.iterrows():
		rl = []
		for j in range(0, 16):
			z = [bool(row[j])]
			rl = rl + z
		h = row[16]
		holref = Holiday.query.filter_by(Code=h).first()
		if len(holref)<1:
			h1 = '00'
		else:
			h1 = holref.id
		if h1 == '00':
			h2 = False
		else:
			h2 = True
		try:
			btp = BookType(Plan=rl[0], ABC=rl[1], Award=rl[2], BegRead=rl[3], Chapter=rl[4],\
				Biography=rl[5], Mystery=rl[6], Folktales=rl[7], Game=rl[8], Season=h2, Code=h1,\
				Paired=rl[9], Poetry=rl[10], Professional=rl[11], Science=rl[12], SharedRd=rl[13], \
				Sports=rl[14], Wordless=rl[15])
			db.session.add(btp)
			db.session.commit()
			numbooks = BookType.query.count()
			numbooks = [numbooks]
			t = t + numbooks
		except:
			mt = 1 + m1
	print(str(mt) + ' BookType Enteries Failed to Load.')
	return t

def bookLoader():
	dp = path + files['bk']
	for df in pd.read_csv(dp, chunksize=ch):
		a = []
		for index, row in df.iterrows():
			af = [row['Author']]
			a = a + af
		addAuthor(a)
		dbf = df[cates]
		bts = addType(dbf)
#		for index, row in df.iterrows():
#			try:

'''
def filldb():
	try:
		addState()
	except:
		print('States Failed to Load')
	try:
		addType()
	except:
		print('Book Types Failed to Load')
	try:
		bookLoader()
	except:
		print('Books Failed to Load')
'''
