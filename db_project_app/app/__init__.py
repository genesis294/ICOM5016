from flask import Flask

app = Flask(__name__)
app.secret_key = "something_secret"
from app import views

