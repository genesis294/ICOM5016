from flask import jsonify
from dao.users import UsersDAO

class UsersHandler:

    def build_users_dict(self, row):
        result = {}
        result['uid'] = row['uid']
        result['fname'] = row['fname']
        result['lname'] = row['lname']
        result['email'] = row['email']
        result['phone'] = row['phone']
        result['password'] = row['password']
        return result

    def build_admins_dict(self, row):
        result = {}
        result['aid'] = row['aid']
        result['uid'] = row['uid']
        result['fname'] = row['fname']
        result['lname'] = row['lname']
        result['email'] = row['email']
        result['phone'] = row['phone']
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['uid'] = row['uid']
        result['sid'] = row['sid']
        result['fname'] = row['fname']
        result['lname'] = row['lname']
        result['email'] = row['email']
        result['phone'] = row['phone']
        result['location'] = row['location']
        result['address'] = row['address']
        result['TBusiness'] = row['TBusiness']
        return result

    def build_person_in_need_dict(self, row):
        result = {}
        result['uid'] = row['uid']
        result['nid'] = row['nid']
        result['fname'] = row['fname']
        result['lname'] = row['lname']
        result['email'] = row['email']
        result['phone'] = row['phone']
        result['location'] = row['location']
        result['address'] = row['address']
        return result

    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_users_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUsersById(self, uid):
        dao = UsersDAO()
        row = dao.getUsersById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            users = self.build_users_dict(row)
            return jsonify(Users = users)

    def searchUsers(self, args):
        fname = args.get("fname")
        lname = args.get("lname")
        dao = UsersDAO()

        if fname and lname:
            users_list = dao.getUsersByfNameAndlName(fname, lname)
        elif fname:
            users_list = dao.getUsersByfName(fname)
        elif lname:
            users_list = dao.getUsersBylName(lname)
        else:
            return jsonify(Error = "Not found"), 404

        result_list = []

        for row in users_list:
            result = self.build_users_dict(row)
            result_list.append(result)

        return jsonify(Users=result_list)

    def getUsersByfName(self, fname):
        dao = UsersDAO()
        users_list = dao.getUsersByfName(fname)

        if not users_list:
            return jsonify(Error="First Name of User not Found"), 404
        else:
            result_list = []

            for row in users_list:
                result = self.build_users_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUsersBylName(self, lname):
        dao = UsersDAO()
        users_list = dao.getUsersBylName(lname)

        if not users_list:
            return jsonify(Error="Last Name of User not Found"), 404
        else:
            result_list = []

            for row in users_list:
                result = self.build_users_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUsersByfNameAndlName(self, fname, lname):
        dao = UsersDAO()
        users_list = dao.getUsersByfNameAndlName(fname, lname)

        if not users_list:
            return jsonify(Error="Full Name of User not Found"), 404
        else:
            result_list = []

            for row in users_list:
                result = self.build_users_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)


# Method to get a user by their email address. (Added by Genesis. Need it for login)
    def getUserByEmail(self, email):
        dao = UsersDAO()
        row = dao.getUsersByEmail(email)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            users = self.build_users_dict(row)
            return jsonify(Users = users)

    def getAllAdmins(self):
        dao = UsersDAO()
        admin_list = dao.getAllAdmins()
        result_list = []
        for row in admin_list:
            result = self.build_admins_dict(row)
            result_list.append(result)
        return jsonify(Admins = result_list)

    def getAdminsById(self, aid):
        dao = UsersDAO()
        row = dao.getAdminById(aid)
        if not row:
            return jsonify(Error = "Admin Not Found"), 404
        else:
            Admins = self.build_admins_dict(row)
           # Users = self.build_users_dict(row)
            return jsonify(Admins = Admins)

    def getAllSuppliers(self):
        dao = UsersDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getSuppliersBySID(self, sid):
        dao = UsersDAO()
        row = dao.getSuppliersBySID(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            suppliers = self.build_supplier_dict(row)
            return jsonify(Suppliers = suppliers)

    def getBusiness(self,TBusiness):
        dao = UsersDAO()
        row = dao.getBusiness(TBusiness)
        if not row:
            return jsonify(Error = "Business Not Found"), 404
        else:
            business = self.build_supplier_dict(row)
            return jsonify(Business = business)

    def getAllPInNeed(self):
        dao = UsersDAO()
        p_in_need_list = dao.getAllPInNeed()
        result_list = []
        for row in p_in_need_list:
            result = self.build_person_in_need_dict(row)
            result_list.append(result)
        return jsonify(PersonInNeed = result_list)

    def getPInNeedByNID(self, sid):
        dao = UsersDAO()
        row = dao.getPInNeedByNID(sid)
        if not row:
            return jsonify(Error = "Person In Need Not Found"), 404
        else:
            PersonInNeed = self.build_person_in_need_dict(row)
            return jsonify(PersonInNeed = PersonInNeed)