#!flask/bin/python
from app import app, lm


app.secret_key = "something_secret"
lm.init_app(app)
lm.login_view = 'login'

app.run(debug=True)