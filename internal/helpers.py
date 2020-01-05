from flask_login import current_user
from internal.messages.reply import *
from internal.models import User
from internal import db
import pandas as pd

class Admin:

	def checkAccess():
		return current_user.usertype >= 3

	def checkAuthority():
		return current_user.usertype > 1

class MSG:

	def body(str1, str2):
		hd = header + str1 + '\n'
		final_String = hd + str2
		return final_String

	def autoReply():
		return reply


class RSG:

	def userCreator(num, str1, str2, str3):
		user = User(Username = str1, email = str2, usertype = num)
		user.set_password(str3)
		db.session.add(user)
		db.session.commit()

class File:

	def modelToPd(md):
		return pd.DataFrame.from_records([i.to_dic() for i in md])
