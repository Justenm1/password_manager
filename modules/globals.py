from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQL database connection
db = SQLAlchemy()
print("administrative: (1) database initialized")

# Flask configuration
app = Flask(__name__, template_folder='../templates', static_folder="../static")

