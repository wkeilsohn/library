from flask import render_template
from internal import app

from internal.forms import LoginForm, AuthorForm, PublisherForm, BookForm, InventoryForm

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
	return render_template('login.html', form = form)

@app.route("/logout/")
def logout():
	return render_template('logout.html')

@app.route("/AddBook/", methods=['GET', 'POST'])
def books():
	form = BookForm()
	return render_template('books.html', form = form)

@app.route("/AddAuthor/", methods=['GET', 'POST'])
def author():
	form = AuthorForm()
	return render_template('author.html', form = form)

@app.route("/AddItem/", methods=['GET', 'POST'])
def item():
	form = InventoryForm()
	return render_template('item.html', form = form)

@app.route("/AddPublisher/", methods=['GET', 'POST'])
def publisher():
	form = PublisherForm()
	return render_template('publish.html', form = form)

'''
@app.route("/Lookup/", methods=['GET', 'POST'])
def loggin():
	form = LookupForm()
	return render_template('lookup.html', form = form)
'''