from flask_login import current_user
from internal.messages.reply import *

class Admin:

	def checkAccess():
		if current_user.usertype >= 3:
			return redirect('/home/')

	def checkAuthority():
		if current_user.usertype == 1:
			return redirect('/home/')

class MSG:

	def body(str1, str2):
		hd = header + str1 + '\n'
		final_String = hd + str2
		return final_String


	def autoReply():
		return reply