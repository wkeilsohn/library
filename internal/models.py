from internal import db

class User(db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User: {}>'.format(self.username) 


class Author(db.Model):
	__tablename__ = 'Author'
	id = db.Column(db.Integer, primary_key=True)
	FirstName = db.Column(db.String(64), index = True)
	MiddleName = db.Column(db.String(64), index = True)
	LastName = db.Column(db.String(100), index = True)
	Book = db.relationship("Book")

	def __repr__(self):
		return '<Author: {} {} {}>'.format(self.FirstName, self.MiddleName, self.LastName)


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
	State = db.Column(db.String(50), db.ForeignKey('State.State'))
	Country = db.Column(db.String(50), index = True)
	Book = db.relationship("Book")

	def __repr__(self):
		return '<Publisher: {}>'.format(self.Publisher)


class Holiday(db.Model):
	__tablename__ = 'Holiday'
	id = db.Column(db.Integer, primary_key = True)
	Name = db.Column(db.String(20), unique = True, index = True)
	Code = db.Column(db.String(5), unique = True, index = True)
	BookType = db.relationship("BookType")

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
	Paired = db.Column(db.Boolean, index = True)
	Poetry = db.Column(db.Boolean, index = True)
	Professional = db.Column(db.Boolean, index = True)
	Science = db.Column(db.Boolean, index = True)
	SharedRd = db.Column(db.Boolean, index = True)
	Sports = db.Column(db.Boolean, index = True)
	Wordless = db.Column(db.Boolean, index = True)
	Holiday = db.Column(db.String(5), db.ForeignKey('Holiday.Code'))
	Book = db.relationship("Book")

	def __repr__(self):
		return '<Row Number: {}>'.format(self.id)


class Book(db.Model):
	__tablename__ = 'Book'
	id = db.Column(db.Integer, primary_key = True)
	LibraryId = db.Column(db.String(400), index =True)
	Title = db.Column(db.String(120), index = True, unique = True)
	FirstAuthor = db.Column(db.String(100), db.ForeignKey('Author.LastName'), index = True)
	SubsequentAuthors = db.Column(db.String(300))
	Publisher = db.Column(db.String(64), db.ForeignKey('Publisher.Publisher'), index = True)
	PublicationYear = db.Column(db.Integer, index = True)
	BookType = db.Column(db.String(5), db.ForeignKey('BookType.Type'))
	Fiction = db.Column(db.Boolean, index = True)
	Inventory = db.relationship("Inventory")

	def __repr__(self):
		return '<Book: {} by {}>'.format(self.Title, self.FirstAuthor)
		

class Inventory(db.Model):
	__tablename__ = 'Inventory'
	id = db.Column(db.Integer, primary_key = True)
	Book = db.Column(db.String(120), db.ForeignKey('Book.Title'), index = True, unique = True)
	Quantity = db.Column(db.Integer)

	def __repr__(self):
		return '<Inventory: {} copies of {}>'.format(self.Quantity, self.Book)

