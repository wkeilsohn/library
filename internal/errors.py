from flask import render_template
from internal import app

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

'''
@app.errorhandler(500)
def not_found_error(error):
	return render_template('500.html'), 500
'''