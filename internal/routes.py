from flask import render_template, flash, redirect, url_for, request
from internal import app
from internal.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from internal.models import User
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/home/")
@login_required
def home():
    return render_template('home.html')

@app.route("/about/")
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
def books():
	form = AddBookForm()
	return render_template('books.html', form = form)

@app.route("/AddAuthor/", methods=['GET', 'POST'])
def author():
	form = AddAuthorForm()
	return render_template('author.html', form = form)

@app.route("/AddItem/", methods=['GET', 'POST'])
def item():
	form = InventoryForm()
	return render_template('item.html', form = form)

@app.route("/AddPublisher/", methods=['GET', 'POST'])
def publisher():
	form = AddPublisherForm()
	return render_template('publisher.html', form = form)

'''
@app.route("/Lookup/", methods=['GET', 'POST'])
def loggin():
	form = LookupForm()
	return render_template('lookup.html', form = form)
'''