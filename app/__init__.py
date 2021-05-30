from flask import Flask

# Create and config flask app
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Import modules


# Init objects


# Import views
from app.views import *
