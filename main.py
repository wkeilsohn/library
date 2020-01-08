from internal import app, db
from internal.models import *

if __name__== "__main__":
	app.run(debug=False)

@app.shell_context_processor
def make_shell_context():
	return {'db': db,
			'Status': Status,
			'User': User,
			'Author': Author,
			'State': State,
			'Publisher':Publisher,
			'Holiday': Holiday,
			'BookType': BookType,
			'Book': Book,
			'Inventory': Inventory}