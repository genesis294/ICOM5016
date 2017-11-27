from flask import render_template
from app import app


@app.route('/')


@app.route('/DisasterSite')
def index():
    return render_template('DisasterSite.html',
                           title='Home',
                           )

