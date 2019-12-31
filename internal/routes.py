from flask import render_template, flash, redirect, url_for, request
from internal import app, db, engine
from internal.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from internal.models import *
from internal.tables import *
from werkzeug.urls import url_parse
import pandas as pd

@app.route("/") # Good...Just add Search/Navigation Features.
@app.route("/home/")
@login_required
def home():
    return render_template('home.html')

@app.route("/about/") # Good!... Just fill out the page.
def about():
	return render_template('about.html')

@app.route("/login/", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect('/home/')
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(Username=form.Username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect('/login/')
		login_user(user)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = 'home.html'
		flash('Login Successful')
		return redirect('/home/')
	return render_template('login.html', form = form)

@app.route("/logout/")
def logout():
	logout_user()
	return render_template('logout.html')

@app.route("/AddBook/", methods=['GET', 'POST'])
@login_required
def books():
	authors = Author.query.all()
	authors = [(i.id, i.LastName) for i in authors]
	publishers = Publisher.query.all()
	publishers = [(i.id, i.Publisher) for i in publishers]
	holidays = Holiday.query.all()
	holidays = [(i.id, i.Name) for i in holidays]
	books = Book.query.all() # Yes, if there are engough books this could become a problem...
	books = [(i.Title) for i in books]
	books = [j.upper() for j in books]
	books = [z.replace(" ", "") for z in books]
	form = AddBookForm()
	form.FirstAuthor.choices = authors
	form.Publisher.choices = publishers
	form.BookType.Holiday.choices = holidays
	if form.validate_on_submit():
		b = form.Title.data
		b = b.upper()
		b = b.replace(" ", "")
		if b in books:
			flash('Book Already in Data Base')
			return redirect('/AddBook/')
		else:
			booktype = BookType(Plan = form.BookType.Plan.data, ABC = form.BookType.ABC.data, Award = form.BookType.Award.data, \
				BegRead = form.BookType.BegRead.data, Chapter = form.BookType.Chapter.data, Biography = form.BookType.Biography.data, \
				Mystery = form.BookType.Mystery.data, Folktales = form.BookType.Folktales.data, Game = form.BookType.Game.data, \
				Season = form.BookType.Season.data, Code = form.BookType.Holiday.data, Paired = form.BookType.Paired.data, \
				Poetry = form.BookType.Poetry.data, Professional = form.BookType.Professional.data, Science = form.BookType.Science.data, \
				SharedRd = form.BookType.SharedRd.data, Sports = form.BookType.Sports.data, Wordless = form.BookType.Wordless.data)
			db.session.add(booktype)
			db.session.commit()
			num = BookType.query.count()
			bookrow = BookType.query.get(num)
			book = Book(LibraryId = form.LibraryId.data, Title = form.Title.data, AuthorId = form.FirstAuthor.data, \
				SubsequentAuthors = form.SubsequentAuthors.data, PublisherId = form.Publisher.data, PublicationYear = form.PublicationYear.data,\
				BookTypeId = bookrow.id, Fiction = form.Fiction.data)
			db.session.add(book)
			db.session.commit()
			flash('Book Added')
			return redirect('/AddBook/')
	return render_template('books.html', form = form)

@app.route("/AddAuthor/", methods=['GET', 'POST'])
@login_required
def author():
	authors = Author.query.all()
	au1 = [(i.FirstName) for i in authors]
	au2 = [(i.LastName) for i in authors]
	authors = [(au1[x] + au2[x]) for x in range(0, len(authors))]
	authors = [j.upper() for j in authors]
	authors = [z.replace(" ", "") for z in authors]
	form = AddAuthorForm()
	if form.validate_on_submit():
		a1 = form.FirstName.data
		a2 = form.LastName.data
		a = a1 + a2
		a = a.upper()
		a = a.replace(" ", "")
		if a in authors:
			flash('Author Already in Data Base')
			return redirect('/AddAuthor/')
		else:
			author = Author(FirstName = form.FirstName.data, MiddleName = form.MiddleName.data, LastName = form.LastName.data)
			db.session.add(author)
			db.session.commit()
			flash('Author Added')
			return redirect('/AddAuthor/')
	return render_template('author.html', form = form)

@app.route("/AddItem/", methods=['GET', 'POST'])
@login_required
def item():
	books = Book.query.all()
	books = [(i.id, i.Title) for i in books]
	mater = Book.query.all()
	mater = [(i.id) for i in mater]
	form = InventoryForm()
	form.Material.choices = books
	if form.validate_on_submit():
		m = form.Material.data
		if m in mater:
			Ib = Inventory.query.filter_by(BookTitle = form.Material.data).first()
			Ib.Quantity = Ib.Quantity + form.Quantity.data
			db.session.commit()
			flash('Inventory Updated')
			return redirect('/AddItem/')
		else:
			item = Inventory(BookTitle = form.Material.data, Quantity = form.Quantity.data)
			db.session.add(item)
			db.session.commit()
			flash('Inventory Added')
			return redirect('/AddItem/')
	return render_template('item.html', form = form)

@app.route("/AddPublisher/", methods=['GET', 'POST'])
@login_required
def publisher():
	states = State.query.all()
	states = [(i.id, i.State) for i in states]
	pubs = Publisher.query.all()
	pubs = [(i.Publisher) for i in pubs]
	pubs = [j.upper() for j in pubs]
	pubs = [z.replace(" ", "") for z in pubs]
	form = AddPublisherForm()
	form.State.choices = states
	if form.validate_on_submit():
		p = form.Publisher.data
		p = p.upper()
		p = p.replace(" ", "")
		if p in pubs:
			flash('Publisher Already in Data Base')
			return redirect('/AddPublisher/')
		else:
			publisher = Publisher(Publisher = form.Publisher.data, City = form.City.data, State = form.State.data, Country = form.Country.data)
			db.session.add(publisher)
			db.session.commit()
			flash('Publisher Added')
			return redirect('/AddPublisher/')
	return render_template('publisher.html', form = form)


@app.route("/Results/", methods=['GET', 'POST'])
@login_required
def results(table):
	return render_template('results.html', table = table)

@app.route("/AuthorSearch/", methods=['GET', 'POST'])
@login_required
def authorsearch():
	form = AuthorLookupForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			FirstName = form.FirstName.data
			MiddleName = form.MiddleName.data
			LastName = form.LastName.data
			filter_data = {'FirstName': FirstName, 'MiddleName': MiddleName, 'LastName': LastName}
			filter_data = {key: value for (key, value) in filter_data.items() if value}
			au = Author.query.filter_by(**filter_data).all() 
			tab = AuthorResults(au)
			return render_template('results.html', table = tab, tp = 'tb')
	return render_template('authorsearch.html', form = form)

@app.route("/PublisherSearch/", methods=['GET', 'POST'])
@login_required
def publishersearch():
	form = PublisherLookupForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			Pub = form.Publisher.data
			City = form.City.data
			Sd = form.State.data
			s = State.query.all()
			Country = form.Country.data
			filter_data = {'Publisher': Pub, 'City': City, 'State': Sd, 'Country': Country}
			filter_data = {key: value for (key, value) in filter_data.items() if value}
			pb = Publisher.query.filter_by(**filter_data).all()
			tpd = pd.DataFrame.from_records([i.to_dic() for i in pb])
			sls = list(tpd.loc[:,'State'])
			stls = list()
			for j in sls:
				z = [s[j-1].Abbreviation]
				stls = stls + z
			tpd['State'] = stls
			tpd = tpd.drop(columns=['id'])
			return render_template('results.html', table = tpd.to_html(), tp = 'str')
	return render_template('publishersearch.html', form = form)

@app.route("/BookSearch/", methods=['GET', 'POST'])
@login_required
def booksearch():
	holidays = Holiday.query.all()
	holidays = [(i.id, i.Name) for i in holidays]
	form = BookLookupForm()
	form.BookType.Holiday.choices = holidays
	if request.method == 'POST':
		if form.validate_on_submit():
			### Search for Book Type First. ###
			Code = form.BookType.Holiday.data
			print(Code)
			bt_data = {'Plan': form.BookType.Plan.data, 'ABC': form.BookType.ABC.data, 'Award': form.BookType.Award.data, \
			'BegRead': form.BookType.BegRead.data, 'Chapter': form.BookType.Chapter.data, 'Biography': form.BookType.Biography.data, \
			'Mystery': form.BookType.Mystery.data, 'Folktales': form.BookType.Folktales, 'Game': form.BookType.Game.data, 'Season': form.BookType.Season.data, \
			'Code': Code, 'Paired': form.BookType.Paired.data, 'Poetry': form.BookType.Poetry.data, 'Professional': form.BookType.Professional.data, \
			'Science': form.BookType.Science.data, 'SharedRd': form.BookType.SharedRd.data, 'Sports': form.BookType.Sports.data, 'Wordless': form.BookType.Wordless.data}
			bt1 = {key: '' for (key, value) in bt_data.items() if value == False}
			bt2 = {key: value for (key, value) in bt_data.items() if value == True}
			bt3 = {key: value for (key, value) in bt_data.items() if isinstance(value, int)}
			bt_data = {**bt1, **bt2, **bt3}
			bt_data = {key: value for (key, value) in bt_data.items() if value}
			print(bt_data)
			btb = BookType.query.filter_by(**bt_data).all()
			btls = [i.id for i in btb]
			print(btls)
			### Then Search for the rest of the book ###
			AuthorId = form.FirstAuthor.data
			A_data = {'LastName': AuthorId}
			A_data = {key: value for (key, value) in A_data.items() if value}
			if len(A_data) > 0:
				a = Author.query.filter_by(**A_data).first() # Yes, it only gets the first, so this isn't optimal.
				if a is None:
					AuthorId = ''
				else:
					AuthorId = a.id
			a = Author.query.all()
			PublisherId = form.Publisher.data
			P_data = {'Publisher': PublisherId}
			P_data = {key: value for (key, value) in P_data.items() if value}
			if len(P_data) > 0:
				p = Publisher.query.filter_by(**P_data).first()  # Same Here.
				if p is None:
					PublisherId = ''
				else:
					PublisherId = p.id
			p = Publisher.query.all()
			Title = form.Title.data
			PublicationYear = form.PublicationYear.data
			if len(PublicationYear) > 0:
				PublicationYear = int(PublicationYear)
			Fiction = form.Fiction.data
			filter_data = {'Title': Title, 'FirstAuthor': AuthorId, 'PublisherId': PublisherId, \
			'PublicationYear': PublicationYear, 'Fiction': Fiction}
			filter_data = {key: value for (key, value) in filter_data.items() if value}
			if len(btls)<=0:
				flash('No results matching that category')
				return render_template('booksearch.html', form = form)
			bb = Book.query.filter_by(**filter_data).filter(Book.BookTypeId.in_(btls)).all() # Lots of filtering.
			tpd = pd.DataFrame.from_records([i.to_dic() for i in bb])
			als = list(tpd.loc[:, 'AuthorId'])
			pls = list(tpd.loc[:, 'PublisherId'])
			lals = list()
			lpls = list()
			lhls = list()
			for j in als:
				z = [a[j-1].LastName]
				lals = lals + z
			for x in pls:
				z = [p[x-1].Publisher]
				lpls = lpls + z
			tpd['AuthorId']=lals
			tpd['PublisherId']=lpls
			tpd.rename({'AuthorId': 'Author Last Name', 'PublisherId': 'Publisher'})
			tpd = tpd.drop(columns=['id'])
			return render_template('results.html', table = tpd.to_html(), tp = 'str')
	return render_template('booksearch.html', form = form)