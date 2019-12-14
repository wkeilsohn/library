from flask import Flask, render_template, request
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from internal import routes, errors