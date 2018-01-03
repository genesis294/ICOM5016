from flask import render_template, request, flash, redirect, url_for, json, jsonify
from handler.resources import ResourcesHandler
from flask_login import login_user, logout_user, login_required
from login_form import LoginForm
from user import User
from app import app, lm
from handler.transactions import TransactionsHandler
from handler.users import UsersHandler
from dao.users import UsersDAO
from dao.resources import ResourcesDAO


# Route for home page
@app.route('/')
def home():
    return render_template('DisasterSite.html')


########################################
#     Routes related to resources      #
#  and general navigation of the site  #
########################################


# ========= General Resources ======== #

# Route for rendering all resources resources page.
@app.route('/resources')
def get_resources():
    return ResourcesHandler().get_all_resources()


# Route for getting a single resource by its id
@app.route('/resources/<int:rid>')
def get_resource_by_id(rid):
    return ResourcesHandler().get_resource_by_id(rid)


# ========= Available Resources ======== #

# Route for rendering the available resources page.
@app.route('/available/all')
def available_res():
    return render_template('resource_list.html', resource_type="available")


# Route for getting complete list of available resources
@app.route('/available', methods=['POST', 'GET'])
def handle_available_resources():
    if request.method == 'GET':
        if request.args:
            return ResourcesHandler().search_for_available(request.args)
        else:
            return ResourcesHandler().get_available_resources()
    elif request.method == 'POST':
        try:
            price = request.form['sprice']
            return ResourcesHandler().insert_available_resource(request.form, price)
        except KeyError:
            return ResourcesHandler().insert_available_resource(request.form, 0)
    else:
        return jsonify(Error="Method Not Allowed"), 405


# Route for getting a single resource by its id
@app.route('/available/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def get_available_by_id(rid):
    if request.method == 'PUT':
        try:
            price = request.form['sprice']
            return ResourcesHandler().update_available_resource(rid, price, request.form)
        except KeyError:
            return ResourcesHandler().update_available_resource(rid, 0, request.form)
    elif request.method == 'DELETE':
        return ResourcesHandler().delete_available_resource(rid)
    return ResourcesHandler().get_available_by_id(rid)


# Route that gets a supplied resource based on category
@app.route('/available/<string:category>')
def get_available_by_category(category):
    if not request.args:
        return ResourcesHandler().get_available_by_category(category)
    else:
        return ResourcesHandler().search_for_available_in_category(category, request.args)


# ========= Requested Resources ======== #

# Route that renders the requested resources
@app.route('/requested/all')
def requested_res():
    return render_template('resource_list.html', resource_type="requested")


# Route that gets all the requested resources
@app.route('/requested', methods=['GET', 'POST'])
def handle_requested_resources():
    if request.method == 'GET':
        if request.args:
            return ResourcesHandler().search_for_request(request.args)
        else:
            return ResourcesHandler().get_requested_resources()
    elif request.method == 'POST':
        return ResourcesHandler().insert_requested_resource(request.form)
    else:
        return jsonify(Error="Method Not Allowed"), 405


# Route that gets a single requested resource
@app.route('/requested/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def get_request_by_id(rid):
    if request.method == 'PUT':
        return ResourcesHandler().update_requested_resource(rid, request.form)
    elif request.method == 'DELETE':
        return ResourcesHandler().delete_requested_resource(rid)
    return ResourcesHandler().get_request_by_id(rid)


# Route that gets a single requested resource based on category
@app.route('/requested/<string:category>')
def get_request_by_id_category(category):
    if request.args:
        return ResourcesHandler().search_for_request_in_category(category, request.args)
    else:
        return ResourcesHandler().get_request_by_category(category)

# ===========Resource Profile =============#


# Route that renders the resource profile HTML template
@app.route('/resource_profile')
def resource_profile():
    return render_template('resource_profile.html')


# =========Resource Purchase ========== #
# Renders purchase HTML template and accepts the amount bought
@app.route('/purchase', methods=['GET', 'PUT'])
def purchase():
    error = None
    if request.method == 'PUT':
        res = ResourcesDAO().getAvailableResourceById(int(request.form["rid"]))
        if int(request.form['amount']) < 0 or int(request.form['amount']) > res["rquantity"]:
            error = "Invalid amount"
        else:
            flash("Purchase completed")
            res["rquantity"] = res["rquantity"] - int(request.form["amount"])
            ResourcesHandler().update_available_quantity(request.form["rid"], res)
            return render_template('purchase.html', error=error, complete="complete", amount=request.form["amount"])
    return render_template("purchase.html", error=error, complete="pending")


# =============Add Resource Page ================ #
# Route that renders the add resource HTML template
@app.route('/add',  methods=['GET', 'POST'])
def add_res():
    if request.method == 'POST':
        return render_template('add_resources.html')
    return render_template('add_resources.html', pending="pending")


##################################
#  Routes related to statistics  #
##################################

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


##################################
#   Routes related to users      #
##################################

# Route that renders the sign up HTML template
@app.route('/signup')
def signup():
    return render_template('sign_up.html')


# Route to handle user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        form = LoginForm(email, password)
        if form.validate_user():
            user = User()
            user.set_user(email)
            login_user(user)
            flash("LOGIN SUCCESSFUL")
            return render_template('user_profile.html')
        else:
            error = "Invalid parameters! Please try again."

    return render_template('log_in.html', error=error)


# Route that handles user log out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


# Route that renders the user profile HTML template
@app.route("/user_profile")
@login_required
def user_profile():
    return render_template("user_profile.html")


# Callback used to reload the user object from the user ID stored in the session.
# It takes the unicode ID of a user, and returns the corresponding user object.
# Returns None if the ID is not valid
@lm.user_loader
def load_user(session_id):
    return User().get_user(session_id)


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


@app.route('/users/admins')
def getAllAdmins():
    if not request.args:
        return UsersHandler().getAllAdmins()


@app.route('/users/admins/<int:aid>')
def getAdminsById(aid):
    return UsersHandler().getAdminById(aid)


@app.route('/users/suppliers', methods = ['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return UsersHandler().insertSuppliers(request.form)
    else:
        if not request.args:
            return UsersHandler().getAllSuppliers()
        else:
            return UsersHandler().searchSuppliers(request.args)

@app.route('/users/suppliers/<int:sid>')
def getSuppliersBySID(sid):
    return UsersHandler().getSuppliersBySID(sid)


@app.route('/users/personinneed')
def getAllPInNeed():
    if not request.args:
        return UsersHandler().getAllPInNeed()


@app.route('/users/personinneed/<int:nid>')
def getPInNeedByNID(nid):
    return UsersHandler().getPInNeedByNID(nid)


#################################
# Routes to search for Business #
#################################

@app.route('/business/<string:TBusiness>')
def getBusiness(TBusiness):
    return UsersHandler().getBusiness(TBusiness)