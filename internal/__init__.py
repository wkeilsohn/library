from flask import Flask, render_template, request
from config import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_mail import Message, Mail

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
engine = db.create_engine(Config.SQLALCHEMY_DATABASE_URI, {}) # Apparently, this shouldn't exist(?)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
csrf = CSRFProtect(app)
mail = Mail(app)

from internal import routes, errors, models, tables, helpers