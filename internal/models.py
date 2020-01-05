from internal import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from internal import login

class Status(db.Model):
	__tablename__ = 'Status'
	id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(10), index=True, unique = True)

	User = db.relationship("User")

	def __repr__(self):
		return '<Type: {}>'.format(self.Name)


class User(UserMixin, db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key=True)
	Username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	usertype = db.Column(db.Integer, db.ForeignKey('Status.id'))
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User: {}>'.format(self.Username) 

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)



class Author(db.Model):
	__tablename__ = 'Author'
	id = db.Column(db.Integer, primary_key=True)
	FirstName = db.Column(db.String(64), index = True)
	MiddleName = db.Column(db.String(64), index = True)
	LastName = db.Column(db.String(100), index = True)

	Book = db.relationship("Book", backref="Author")

	def __repr__(self):
		return '<Author: {} {} {}>'.format(self.FirstName, self.MiddleName, self.LastName)

	def to_dic(self):
		return{'id': self.id, 'First_Name': self.FirstName, 'Middle_Name': self.MiddleName, 'Last_Name': self.LastName}


class State(db.Model):
	__tablename__ = 'State'
	id = db.Column(db.Integer, primary_key = True)
	State = db.Column(db.String(50), index = True, unique = True)
	Abbreviation = db.Column(db.String(2), index = True, unique = True)

	Publisher = db.relationship("Publisher")

	def __repr__(self):
		return '<State: {}>'.format(self.State)


class Publisher(db.Model):
	__tablename__ = 'Publisher'
	id = db.Column(db.Integer, primary_key=True)
	Publisher = db.Column(db.String(64), index=True, unique=True)
	City = db.Column(db.String(64), index = True)
	State = db.Column(db.Integer, db.ForeignKey('State.id'))
	Country = db.Column(db.String(50), index = True)

	Book = db.relationship("Book", backref="Publisher")

	def __repr__(self):
		return '<Publisher: {}>'.format(self.Publisher)

	def to_dic(self):
		return {'id': self.id, 'Publisher': self.Publisher, 'City': self.City, 'State': self.State, 'Country': self.Country}


class Holiday(db.Model):
	__tablename__ = 'Holiday'
	id = db.Column(db.Integer, primary_key = True)
	Name = db.Column(db.String(20), unique = True, index = True)
	Code = db.Column(db.String(5), unique = True, index = True)

	BookType = db.relationship("BookType", backref="Holiday")

	def __repr__(self):
		return '<Holiday: {}>'.format(self.Name)


class BookType(db.Model):
	__tablename__ = 'BookType'
	id = db.Column(db.Integer, primary_key = True)
	Plan = db.Column(db.Boolean, index = True)
	ABC = db.Column(db.Boolean, index = True)
	Award = db.Column(db.Boolean, index = True)
	BegRead = db.Column(db.Boolean, index = True)
	Chapter = db.Column(db.Boolean, index = True)
	Biography = db.Column(db.Boolean, index = True)
	Mystery = db.Column(db.Boolean, index = True)
	Folktales = db.Column(db.Boolean, index = True)
	Game = db.Column(db.Boolean, index = True)
	Season = db.Column(db.Boolean, index = True)
	Code = db.Column(db.Integer, db.ForeignKey('Holiday.id'))
	Paired = db.Column(db.Boolean, index = True)
	Poetry = db.Column(db.Boolean, index = True)
	Professional = db.Column(db.Boolean, index = True)
	Science = db.Column(db.Boolean, index = True)
	SharedRd = db.Column(db.Boolean, index = True)
	Sports = db.Column(db.Boolean, index = True)
	Wordless = db.Column(db.Boolean, index = True)

	Book = db.relationship("Book", backref="BookType")

	def __repr__(self):
		return '<Row Number: {}>'.format(self.id)

	def to_dic(self):
		return{'id': self.id, "Plan": self.Plan, "ABC": self.ABC, "Award": self.Award, "BegRead": self.BegRead, \
		"Chapter": self.Chapter, "Biography": self.Biography, "Mystery": self.Mystery, "Folktales": self.Folktales, \
		"Game": self.Game, "Season": self.Season, "Code":self.Code, "Paired":self.Paired, "Poetry":self.Poetry, \
		"Professional": self.Professional, "Science": self.Science, "SharedRd": self.SharedRd, "Sports": self.Sports, \
		"Wordless": self.Wordless}


class Book(db.Model):
	__tablename__ = 'Book'
	id = db.Column(db.Integer, primary_key = True)
	LibraryId = db.Column(db.String(100), index =True)
	Title = db.Column(db.String(120), index = True, unique = True)
	AuthorId = db.Column(db.Integer, db.ForeignKey('Author.id'), index = True)
	SubsequentAuthors = db.Column(db.String(300))
	PublisherId = db.Column(db.Integer, db.ForeignKey('Publisher.id'), index = True)
	PublicationYear = db.Column(db.Integer, index = True)
	BookTypeId = db.Column(db.Integer, db.ForeignKey('BookType.id'))
	Fiction = db.Column(db.Boolean, index = True)

	Inventory = db.relationship("Inventory", backref="Book")

	def __repr__(self):
		return '<Book: {} by {}>'.format(self.Title, self.AuthorId)

	def to_dic(self):
		return{'id': self.id, 'LibraryId': self.LibraryId, 'Title': self.Title, 'AuthorId': self.AuthorId, 'SubsequentAuthors': self.SubsequentAuthors, \
		'PublisherId': self.PublisherId, 'PublicationYear': self.PublicationYear, 'BookTypeId': self.BookTypeId, 'Fiction': self.Fiction}
		

class Inventory(db.Model):
	__tablename__ = 'Inventory'
	id = db.Column(db.Integer, primary_key = True)
	BookTitle = db.Column(db.Integer, db.ForeignKey('Book.Title'), index = True) # Come back later for an update!
	Quantity = db.Column(db.Integer)

	def __repr__(self):
		return '<Inventory: {} copies of {}>'.format(self.Quantity, self.BookTitle)

	def to_dic(self):
		return{'id': self.id, 'BookTitle': self.BookTitle, 'Quantity': self.Quantity}

@login.user_loader
def load_user(id):
    return User.query.get(int(id))