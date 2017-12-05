from flask import render_template, request, flash, redirect, url_for, json

from dao.resources import ResourcesDAO
from handler.resources import ResourcesHandler
from handler.users import UsersHandler

from app import app

# Route for home page
from handler.transactions import TransactionsHandler


@app.route('/')
def home():
    return render_template('DisasterSite.html')


#####################################
# Routes to search for resources    #
#####################################

# Route for rendering the available resources page.
@app.route('/available')
def available_res():
    if not request.args:
        return render_template('resource_list.html', resource_type="available")
    else:
        return ResourcesHandler().search_for_available(request.args)


# Route for getting complete list of available resources
@app.route('/available/all')
def get_all_resources():
    return ResourcesHandler().get_available_resources()


# Route for getting a single resource by its id
@app.route('/available/<int:rid>')
def get_available_by_id(rid):
    return ResourcesHandler().get_available_by_id(rid)


# Route that renders the requested resources
@app.route('/requested')
def requested_res():
    if not request.args:
        return render_template('resource_list.html', resource_type="requested")
    else:
        return ResourcesHandler().search_for_request(request.args)


# Route that gets all the requested resources
@app.route('/requested/all')
def get_all_req_resources():
    return ResourcesHandler().get_requested_resources()


# Route that gets a single requested resource
@app.route('/requested/<int:rid>')
def get_request_by_id(rid):
    return ResourcesHandler().get_request_by_id(rid)


# Route that renders the resource profile HTML template
@app.route('/resource_profile')
def resource_profile():
    return render_template('resource_profile.html')


# Route that renders the add resource HTML template
@app.route('/add')
def add_res():
    return render_template('add_resources.html')


# Route that renders the daily statistics HTML template
@app.route('/dailyStats')
def daily_stats():
    return render_template('statistics.html', stats="daily")


# Route that gets the daily stats
@app.route('/dailyStats/get')
def get_daily_stats():
    return ResourcesHandler().get_daily_stats()


# Route that renders the regional statistics HTML template
@app.route('/regionStats')
def region_stats():
    return render_template('region_statistics.html', stats="region")


# Route that gets the regional statistics
@app.route('/regionStats/get')
def get_region_stats():
    return ResourcesHandler().get_regional_stats()


# Route that renders the weekly statistics HTML template
@app.route('/weeklyStats')
def weekly_stats():
    return render_template('statistics.html', stats="weekly")


# Route that gets the weekly stats
@app.route('/weeklyStats/get')
def get_weekly_stats():
    return ResourcesHandler().get_weekly_stats()


# Route that renders the sign up HTML template
@app.route('/signup')
def signup():
    return render_template('sign_up.html')


# Route that renders the login HTML template
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != "test" or request.form['password'] != "test":
            error = "Invalid parameters! Please try again."
        else:
            flash("LOGIN SUCCESSFUL")
            return render_template('user_profile.html')

        # email = request.form['email']
        # user = UsersHandler().getUserByEmail(email)
        # password = request.form['password']
        # if user and if user

    return render_template('log_in.html', error=error)


# Renders purchase HTML template and accepts the amount bought
@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    error = None
    if request.method == 'POST':
        res = ResourcesDAO().getAvailableResourceById(int(request.form["rid"]))
        if int(request.form['amount']) < 0 or int(request.form['amount']) > res["rquantity"]:
            error = "Invalid amount"
        else:
            flash("Purchase completed")
            res["rquantity"] = res["rquantity"] - int(request.form["amount"])
            ResourcesHandler().update_available(request.form["rid"], res)
            return render_template('purchase.html', error=error, complete="complete", amount=request.form["amount"])
    return render_template("purchase.html", error=error, complete="pending")


#####################################
# Routes to search for transactions #
#                                   #
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
