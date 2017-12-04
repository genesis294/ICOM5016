from flask import render_template, request
from handler.resources import ResourcesHandler

from app import app

# Route for home page
from handler.transactions import TransactionsHandler
from handler.users import UsersHandler

@app.route('/')
def home():
    return render_template('DisasterSite.html')

# Route for available resources page
@app.route('/available')
def available_res():
    if not request.args:
        return render_template("available_resources.html")
    else:
        return ResourcesHandler().search_for_available(request.args)


@app.route('/available/all')
def get_all_resources():
    return ResourcesHandler().get_available_resources()


@app.route('/available/<int:rid>')
def get_available_by_id(rid):
    return ResourcesHandler().get_available_by_id(rid)


@app.route('/requested')
def requested_res():
    #return render_template('requested_resources.html')
    if not request.args:
        return ResourcesHandler().get_requested_resources()
    else:
        return ResourcesHandler().search_for_request(request.args)


@app.route('/requested/<int:rid>')
def get_request_by_id(rid):
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


#####################################
# Routes to search for transactions #
#      (For testing purposes)       #
#####################################
@app.route('/transactions')
def getAllTransactions():
    if not request.args:
        return TransactionsHandler().getAllTransactions()
    else:
        return TransactionsHandler().searchTransactions(request.args)


@app.route('/transactions/<int:tid>')
def getTransactionByID(tid):
    return TransactionsHandler().getTransactionByID(tid)


@app.route('/transactions/user/<int:uid>')
def getTransactionsByUserID(uid):
    return TransactionsHandler().getTransactionsByUserID(uid)


@app.route('/transactions/cart/<int:cid>')
def getTransactionsByCartID(cid):
    return TransactionsHandler().getTransactionsByCartID(cid)

##############################
# Routes to search for Users #
##############################

@app.route('/users')
def getAllUsers():
    if not request.args:
        return UsersHandler().getAllUsers()
    else:
        return UsersHandler().searchUsers(request.args)

@app.route('/users/<int:uid>')
def getUsersById(uid):
    return UsersHandler().getUsersById(uid)

@app.route('/users/fname/<string:fname>')
def getUsersByfName(fname):
    return UsersHandler().getUsersByfName(fname)

@app.route('/users/lname/<string:lname>')
def getUsersBylName(lname):
    return UsersHandler().getUsersBylName(lname)

@app.route('/users/fname/<string:fname>/lname/<string:lname>')
def getUsersByfNameAndlName(fname, lname):
    return UsersHandler().getUsersByfNameAndlName(fname,lname)