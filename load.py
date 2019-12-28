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


def addHolidays():
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

def checkUniqueAuthor(a = '', b='', c=''):
	Au_data = {'FirstName': a, 'MiddleName': b, 'LastName': c}
	Au_data = {key: value for (key, value) in Au_data.items() if value}
	au = Author.query.filter_by(**Au_data).all()
	if len(au) == 0:
		return True
	else:
		return False

def addAuthor(au):
	ma = 0
	aid = 0
	aua = ''
	if isinstance(au, str):
		name = re.split(', |. |& |.', au)
		lm = name[0]
		fm = name[1]
		if au.find('&') > -1 and len(name) > 4:
			if len(name[2]) == 1:
				mm = name[2]
				for j in range(4, len(name)):
					aua = aua + name[j]
			else:
				mm = ''
		elif len(name) == 3 and au.find('&') == -1:
			mm = name[2]
		else:
			mm = ''
	else:
		fm = ''
		mm = ''
		lm = 'Unknown'
	if checkUniqueAuthor(fm, mm, lm):
		try:
			a = Author(FirstName=fm, MiddleName=mm, LastName=lm)
			db.session.add(a)
			db.session.commit()
			aid = Author.query.count()
		except:
			ma = ma + 1
	else:
		A_data = {'FirstName': fm, 'MiddleName': mm, 'LastName': lm}
		A_data = {key: value for (key, value) in A_data.items() if value}
		a = Author.query.filter_by(**A_data).first()
		aid = a.id
	return aid, ma, aua

def uniqueBookChecker(st):
	bkdb = Book.query.filter_by(Title=st).all() # Yes, there should be more done to check if the book is in the system, but this is a good starting point.
	if len(bkdb) > 0:
		return False
	else:
		return True

def addType(df):
	mt = 0
	t = 0
	rl = []
	for j in range(0, 16):
		z = [bool(df.iloc[j])]
		rl = rl + z
	h = df[16]
	holref = Holiday.query.filter_by(Code=h).first()
	if holref is None:
		h1 = '00' # Edge case...-_-
	elif len(holref)<1:
		h1 = '00'
	else:
		h1 = holref.Code
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
		t = BookType.query.count()
	except:
		mt = 1 + m1
	return t, mt


def addPublisher():
	# as there is no publication data, only a blank/default publisher will be added.
	p = Publisher(Publisher = 'Unknown', State = 1) # This fails.
	db.session.add(p)
	db.session.commit()

def bookLoader():
	anum = 0
	tynum = 0
	bnum = 0
	dups = 0
	dp = path + files['bk']
	for df in pd.read_csv(dp, chunksize=ch):
		for index, row in df.iterrows():
			bkt = row['Title']
			if uniqueBookChecker(bkt):
				af = row[2]
				aid = addAuthor(af)
				dbf = row[cates]
				bts = addType(dbf)
				fdata = bool(row['Fiction'])
				tynum = tynum + bts[1]
				anum = anum + aid[1]
				# addPublisher(): # There is no publication information.
				try:
					bbk = Book(LibraryId = row['Book_ID'], Title = bkt, AuthorId = aid[0], \
						SubsequentAuthors = aid[2], PublisherId=1, BookTypeId=bts[0], Fiction=fdata)
					db.session.add(bbk)
					db.session.commit()
				except:
					bnum = bnum + 1
			else:
				dups = dups + 1
				continue
	print('A total of ' + str(tynum) + ' book types could not be added; ' \
		+ str(anum) + ' authors could not be added; ' \
		+ str(bnum) + ' books could not be added;' \
		+ str(dups) + ' duplicates are present in the data.')



def filldb():
	try:
		addState()
	except:
		print('States Failed to Load')
	try:
		addHolidays()
	except:
		print('Book Types Failed to Load')
	try:
		addPublisher()
		bookLoader()
	except:
		print('Books Failed to Load')
