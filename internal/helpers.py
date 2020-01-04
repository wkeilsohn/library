from flask_login import current_user
from internal.messages.reply import *

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
		if Admin.checkPrivledge():
			return redirect('/home/')

class MSG:

	def body(str1, str2):
		hd = header + str1 + '\n'
		final_String = hd + str2
		return final_String


	def autoReply():
		return reply