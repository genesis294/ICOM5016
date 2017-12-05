from flask import Flask
from flask_login import login_manager

app = Flask(__name__)
lm = login_manager.LoginManager()

from app import views  # NO BORRAR!