from flask import Flask
from flask_login import login_manager

app = Flask(__name__)

lm = login_manager.LoginManager()

app.secret_key = "something_secret"

from app import views  # NO BORRAR!