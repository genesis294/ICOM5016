from flask import jsonify
from dao.users import UsersDAO


class UsersHandler:

    def build_users_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['email'] = row[3]
        result['upassword'] = row[4]
        return result

    def build_admins_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['email'] = row[3]
        result['upassword'] = row[4]
        result['aid'] = row[5]
        result['phone_id'] = row[6]
        result['phone'] = row[7]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['email'] = row[3]
        result['upassword'] = row[4]
        result['sid'] = row[5]
        result['sbusiness_type'] = row[6]
        result['address_id'] = row[7]
        result['line1'] = row[8]

        result['line2'] = row[9]
        line2 = row[9]
        if not line2:
            result['line2'] = "None"

        result['city'] = row[10]
        result['state'] = row[11]
        result['zipcode'] = row[12]
        result['location_id'] = row[13]
        result['latitude'] = row[14]
        result['longitud'] = row[15]
        result['phone_id'] = row[16]
        result['phone'] = row[17]
        return result

    def build_person_in_need_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['email'] = row[3]
        result['upassword'] = row[4]
        result['nid'] = row[5]
        result['address_id'] = row[6]
        result['line1'] = row[7]

        result['line2'] = row[8]
        line2 = row[8]
        if not line2:
            result['line2'] = "None"

        result['city'] = row[9]
        result['state'] = row[10]
        result['zipcode'] = row[11]
        result['location_id'] = row[12]
        result['latitude'] = row[13]
        result['longitud'] = row[14]
        result['phone_id'] = row[15]
        result['phone'] = row[16]
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
        email = args.get("email")
        dao = UsersDAO()

        if fname and lname:
            users_list = dao.getUsersByfNameAndlName(fname, lname)
        elif fname:
            users_list = dao.getUsersByfName(fname)
        elif lname:
            users_list = dao.getUsersBylName(lname)
        elif email:
            users_list = dao.getUserByEmail(email)
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

    def getUserByEmail(self, email):
        dao = UsersDAO()
        row = dao.getUsersByEmail(email)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            users = self.build_users_dict(row)
            return jsonify(Users = users)


# ADMINS
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
        return jsonify(Admins = Admins)

# SUPPLIERS
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

    def searchSuppliers(self, args):
        city = args.get("city")
        dao = UsersDAO()
        supplier_list = []
        if city:
            supplier_list = dao.getSuppliersByCity(city)
        else:
            return jsonify(Error = "Malformed search string."), 400

        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getBusiness(self, TBusiness):
        dao = UsersDAO()
        row = dao.getBusiness(TBusiness)
        if not row:
            return jsonify(Error = "Business Not Found"), 404
        else:
            business = self.build_supplier_dict(row)
            return jsonify(Business = business)

# PERSONS IN NEED
    def getAllPInNeed(self):
        dao = UsersDAO()
        p_in_need_list = dao.getAllPInNeed()
        result_list = []
        for row in p_in_need_list:
            result = self.build_person_in_need_dict(row)
            result_list.append(result)
        return jsonify(PersonInNeed = result_list)

    def getPInNeedByNID(self, nid):
        dao = UsersDAO()
        row = dao.getPInNeedByNID(nid)
        if not row:
            return jsonify(Error = "Person In Need Not Found"), 404
        else:
            person = self.build_person_in_need_dict(row)
        return jsonify(PersonInNeed = person)
