from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object("project.config.Config")
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
from . import routes
