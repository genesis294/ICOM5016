from flask import render_template, request, flash, redirect, url_for
from handler.resources import ResourcesHandler
from flask_login import login_user, logout_user, login_required
from login_form import LoginForm
from user import User
from app import app, lm
from handler.transactions import TransactionsHandler
from handler.users import UsersHandler

from dao.users import UsersDAO


# Route for home page
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
    # return render_template('requested_resources.html')
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


# Route to handle user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        form = LoginForm(email, password)
        if form.validate_on_submit():       # returns: None if user does not exist; the user dictionary otherwise
            user = User(form.validate_on_submit())
            login_user(user)
            flash("LOGIN SUCCESSFUL")
            return render_template('user_profile.html')
        else:
            error = "Invalid parameters! Please try again."

    return render_template('log_in.html', error=error)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


# This callback is used to reload the user object from the user ID stored in the session.
# It takes the unicode ID of a user, and returns the corresponding user object.
# Returns None if the ID is not valid
@lm.user_loader
def load_user(uid):
    udao = UsersDAO()
    return udao.getUsersById(uid)


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