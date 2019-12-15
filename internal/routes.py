from flask import render_template, flash, redirect, url_for
from internal import app

from internal.forms import *

@app.route("/")
@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/about/")
def about():
	return render_template('about.html')

@app.route("/login/", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login Successful')
		return redirect('home.html')
	return render_template('login.html', form = form)

@app.route("/logout/")
def logout():
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