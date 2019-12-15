from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FormField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    Username = StringField('Username', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Submit = SubmitField('Sign In')

class AuthorForm(FlaskForm):
	FirstName = StringField('First Name', validators=[DataRequired()])
	MiddleName = StringField('Middle Name')
	LastName = StringField('Last Name', validators=[DataRequired()])

class PublisherForm(FlaskForm):
	Publisher = StringField('Name of Publisher', validators=[DataRequired()])
	City = StringField('City', validators=[DataRequired()])
	State = StringField('State/Province', validators=[DataRequired()])
	Country = StringField('Country', validators=[DataRequired()])

class BookForm(FlaskForm):
	DCC = StringField('DCC Code', validators=[DataRequired()])
	Title = StringField('Title', validators=[DataRequired()])
	PublicationYear = IntegerField('Publication Year', validators=[DataRequired()])
	FirstAuthor = FormField(AuthorForm)
	SubsequentAuthors = StringField('Additional Authors')
	Publisher = FormField(PublisherForm)

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