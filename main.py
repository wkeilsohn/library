from internal import app, db
from internal.models import *

### Remember to Switch this off ###
app.run(debug=True)
###             ###             ###

@app.shell_context_processor
def make_shell_context():
	return {'db': db,
			'User': User}