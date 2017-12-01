from flask import render_template, request
from handler.resources import ResourcesHandler

from app import app


@app.route('/')
def home():
    return render_template('DisasterSite.html')


@app.route('/available')
def available_res():
    if not request.args:
        return ResourcesHandler().get_available_resources()
    else:
        return ResourcesHandler().search_for_request(request.args)


@app.route('/available/<int:rid>')
def getAvailableById(rid):
    return ResourcesHandler().get_available_by_id(rid)

@app.route('/requested')
def requested_res():
    #return render_template('requested_resources.html')
    if not request.args:
        return ResourcesHandler().get_requested_resources()
    else:
        return ResourcesHandler().search_for_request(request.args)



@app.route('/requested/<int:rid>')
def getRequestById(rid):
    return ResourcesHandler().get_request_by_id(rid)

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


@app.route('/weeklyStats')
def weekly_stats():
    return render_template('seven_day_statistics.html')


@app.route('/signup')
def signup():
    return render_template('sign_up.html')


