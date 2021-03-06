from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FormField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from internal.models import User

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
	Holiday = SelectField('Holiday Code:', coerce = int)
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
	Material = SelectField('Book Title', coerce = int) 
	Quantity = IntegerField('Number of Books', validators=[DataRequired()])
	Submit = SubmitField('Add Item')

class AuthorLookupForm(FlaskForm):
	FirstName = StringField('First Name')
	MiddleName = StringField('Middle Name')
	LastName = StringField('Last Name')
	Submit = SubmitField('Search')

class PublisherLookupForm(FlaskForm):
	Publisher = StringField('Name of Publisher')
	City = StringField('City')
	State = StringField('State/Province')
	Country = StringField('Country')
	Submit = SubmitField('Search')

class BookLookupForm(FlaskForm):
	Title = StringField('Title')
	FirstAuthor = StringField('First Author Last Name')
	Publisher = StringField('Publisher')
	PublicationYear = StringField('Publication Year')
	BookType = FormField(BookTypeForm)
	Fiction = BooleanField('Fiction?')
	Submit = SubmitField('Search')

class ContactForm(FlaskForm):
	Email = StringField('Email',  validators=[DataRequired(), Email()])
	Subject = StringField('Subject',  validators=[DataRequired()])
	Message = TextAreaField('Message',  validators=[DataRequired()])
	Submit = SubmitField('Send')

class RegistrationForm(FlaskForm):
	Username = StringField('Username', validators=[DataRequired()])
	Email = StringField('Email',  validators=[DataRequired(), Email()])
	Password1 = StringField('Password', validators=[DataRequired()])
	Password2 = StringField('Re-Enter Password', validators=[DataRequired(), EqualTo('Password1')])
	Submit = SubmitField('Submit')

	def validate_username(self, Username):
		user = User.query.filter_by(Username=Username.data).first()
		if user is not None:
			raise ValidationError('That Username is already taken.')


	def validate_email(self, Email):
		user = User.query.filter_by(email=Email.data).first()
		if user is not None:
			raise ValidationError('That email address has already been used.')

class DeleteForm(FlaskForm):
	Title = SelectField('Book Title', coerce = int)
	Option = SelectField('Remove', coerce = int) 
	Submit = SubmitField('Delete')

class DeleteUserForm(FlaskForm):
	Username = StringField('Username', validators=[DataRequired()])
	Password = StringField('Password', validators=[DataRequired()])
	Submit = SubmitField('Confirm')