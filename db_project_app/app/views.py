from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('DisasterSite.html')


@app.route('/home')
def home():
    return render_template('DisasterSite.html')


@app.route('/available')
def available_res():
    return render_template('available_resources.html')


@app.route('/add')
def add_res():
    return render_template('add_resources.html')


@app.route('/dailyStats')
def daily_stats():
    return render_template('daily_statistics.html')


@app.route('/login')
def login():
    return render_template('log_in.html')


@app.route('/regionStats')
def region_stats():
    return render_template('region_statistics.html')


@app.route('/requested')
def requested_res():
    return render_template('requested_resources.html')


@app.route('/weeklyStats')
def weekly_stats():
    return render_template('seven_day_statistics.html')


@app.route('/signup')
def signup():
    return render_template('sign_up.html')


