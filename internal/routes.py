from flask import render_template, flash, redirect, url_for, request
from internal import app, db
from internal.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from internal.models import *
from werkzeug.urls import url_parse

@app.route("/") # Good...Just add Search/Navigation Features.
@app.route("/home/")
@login_required
def home():
    return render_template('home.html')

@app.route("/about/") # Good!... Just fill out the page.
def about():
	return render_template('about.html')

@app.route("/login/", methods=['GET', 'POST']) # Good!
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

@app.route("/logout/") # Good!
def logout():
	logout_user()
	return render_template('logout.html')

@app.route("/AddBook/", methods=['GET', 'POST']) # Issue putting the data into the database...
def books():
	authors = Author.query.all()
	authors = [(i.id, i.LastName) for i in authors]
	publishers = Publisher.query.all()
	publishers = [(i.id, i.Publisher) for i in publishers]
	form = AddBookForm()
	form.FirstAuthor.choices = authors
	form.Publisher.choices = publishers
	if form.validate_on_submit():
		booktype = BookType(Plan = form.BookType.Plan.data, ABC = form.BookType.ABC.data, Award = form.BookType.Award.data, \
			BegRead = form.BookType.BegRead.data, Chapter = form.BookType.Chapter.data, Biography = form.BookType.Biography.data, \
			Mystery = form.BookType.Mystery.data, Folktales = form.BookType.Folktales.data, Game = form.BookType.Game.data, \
			Season = form.BookType.Season.data, Code = form.BookType.Holiday.data, Paired = form.BookType.Paired.data, \
			Poetry = form.BookType.Poetry.data, Professional = form.BookType.Professional.data, Science = form.BookType.Science.data, \
			SharedRd = form.BookType.SharedRd.data, Sports = form.BookType.Sports.data, Wordless = form.BookType.Wordless.data)
		db.session.add(booktype)
		db.session.commit()
		num = BookType.query.count()
		bookrow = BookType.query.get(num)# Note that up until this section (below) it works.
		book = Book(LibraryId = form.LibraryId.data, Title = form.Title.data, AuthorId = form.FirstAuthor.data, \
			SubsequentAuthors = form.SubsequentAuthors.data, PublisherId = form.Publisher.data, PublicationYear = form.PublicationYear.data,\
			BookTypeId = bookrow.id, Fiction = form.Fiction.data)
		db.session.add(book)
		db.session.commit()
		flash('Book Added')
		return redirect('/AddBook/')
	return render_template('books.html', form = form)

@app.route("/AddAuthor/", methods=['GET', 'POST']) # Good!
def author():
	form = AddAuthorForm()
	if form.validate_on_submit():
		author = Author(FirstName = form.FirstName.data, MiddleName = form.MiddleName.data, LastName = form.LastName.data)
		db.session.add(author)
		db.session.commit()
		flash('Author Added')
		return redirect('/AddAuthor/')
	return render_template('author.html', form = form)

@app.route("/AddItem/", methods=['GET', 'POST'])
def item():
	return render_template('item.html', form = form)

@app.route("/AddPublisher/", methods=['GET', 'POST']) # Good!
def publisher():
	states = State.query.all()
	states = [(i.id, i.State) for i in states]
	form = AddPublisherForm()
	form.State.choices = states
	if form.validate_on_submit():
		publisher = Publisher(Publisher = form.Publisher.data, City = form.City.data, State = form.State.data, Country = form.Country.data)
		db.session.add(publisher)
		db.session.commit()
		flash('Publisher Added')
		return redirect('/AddPublisher/')
	return render_template('publisher.html', form = form)

'''
@app.route("/Lookup/", methods=['GET', 'POST'])
def loggin():
	form = LookupForm()
	return render_template('lookup.html', form = form)
'''