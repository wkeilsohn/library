from flask_login import current_user

class Admin:
	
	def checkPrivledge():
		cut = current_user.usertype
		if cut < 3:
			return False # Not intuative, but easier to integrate.
		else:
			return True

	def checkAdmin():
		cut = current_user.usertype
		if cut == 1:
			return True
		else:
			return False

	def checkAccess():
		if checkPrivledge():
			return redirect('/home/')
