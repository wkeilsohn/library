from flask_table import Table, Col, BoolCol

class AuthorResults(Table):
	id = Col('id', show = False)
	FirstName = Col('First Name')
	MiddleName = Col('Middle Name')
	LastName = Col('Last Name')

class PublisherResults(Table):
	id = Col('id', show = False)
	Publisher = Col('Publisher')
	City = Col('City')
	State = Col('State/Province')
	Country = Col('Country')


class BookResults(Table):
	id = Col('id', show = False)
	LibraryId = Col('Library Id')
	Title = Col('Title')
	AuthorId = Col('Author')
	SubsequentAuthors = Col('Additional Authors', show = False)
	PublisherId = Col('Publisher')
	PublicationYear = Col('Publication Year')
	BookTypeId = Col('Book Type', show = False)
	Fiction = BoolCol('Fiction')
