from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FormField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    Username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    Submit = SubmitField('Sign In')

class AuthorForm(FlaskForm):
	FirstName = StringField('First Name', validators=[DataRequired()])
	MiddleName = StringField('Middle Name')
	LastName = StringField('Last Name', validators=[DataRequired()])

class PublisherForm(FlaskForm):
	Publisher = StringField('Name of Publisher', validators=[DataRequired()])
	City = StringField('City')
	State = SelectField('State/Province', coerce = int)
	Country = StringField('Country')

class BookTypeForm(FlaskForm):
	Plan = BooleanField('Plan Book?')
	ABC = BooleanField('ABC Book?')
	Award = BooleanField('Award Book?')
	BegRead = BooleanField('Beg. Reading Book?')
	Chapter = BooleanField('Chapter Book?')
	Biography = BooleanField('Biography Book?')
	Mystery = BooleanField('Mystery Book?')
	Folktales = BooleanField('Folktale Book?')
	Game = BooleanField('Game Book?')
	Season = BooleanField('Season Book?')
	Holiday = StringField('Holiday Code')
	Paired = BooleanField('Paired Book?')
	Poetry = BooleanField('Poetry Book?')
	Professional = BooleanField('Professional Book?')
	Science = BooleanField('Science Book?')
	SharedRd = BooleanField('Shared Rd. Book?')
	Sports = BooleanField('Sports Book?')
	Wordless = BooleanField('Wordless Book?')

class BookForm(FlaskForm):
	LibraryId = StringField('Library ID', validators=[DataRequired()])
	Title = StringField('Title', validators=[DataRequired()])
	FirstAuthor = SelectField('First Author', coerce = int)
	SubsequentAuthors = StringField('Additional Authors')
	Publisher = SelectField('Publisher', coerce = int)
	PublicationYear = IntegerField('Publication Year', validators=[DataRequired()])
	BookType = FormField(BookTypeForm)
	Fiction = BooleanField('Fiction?')

class AddAuthorForm(AuthorForm):
	Submit = SubmitField('Add Author')

class AddPublisherForm(PublisherForm):
	Submit = SubmitField('Add Publisher')

class AddBookForm(BookForm):
	Submit = SubmitField('Add Book')

class InventoryForm(FlaskForm):
	Material = FormField(BookForm) # This may need to become a look up of some sort later. 
	Quantity = IntegerField('Number of Books', validators=[DataRequired()])
	Submit = SubmitField('Add Item')

'''
class LookupForm(FlaskForm):
	# Add Fields
	submit = SubmitField('Search')
'''