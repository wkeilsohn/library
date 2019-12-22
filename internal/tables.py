from flask_table import Table, Col

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
	SubsequentAuthors = Col('Additional Authors')
	PublisherId = Col('Publisher')
	PublicationYear = Col('Publication Year')
	BookTypeId = Col('Book Type')
	Fiction = Col('Fiction')
