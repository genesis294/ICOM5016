from flask import jsonify
from dao.users import UsersDAO

class UsersHandler:
    def build_users_dict(self):
        result = {}
        result['uid'] = row['uid']
        result['fname'] = row['fname']
        result['lname'] = row['lname']
        result['email'] = row['emai']
        result['phone'] = row['phone']
        result['password'] = row['password']
        return result

    def build_supplier_dict(self):
        result = {}
        result['location'] = row['location']
        result['address'] = row['address']
        result['TBusiness'] = row['TBusiness']
        return result

    def build_person_in_need_dict(self):
        result = {}
        result['location'] = row['location']
        result['address'] = row['address']

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
        row = dao.getUsersId(uid)
        if not row:
            return jsonify(Error = "User Not FOund"), 404
        else:
            users = self.build_users_dict()
            return jsonify(Users = users)

    def searchUsers(self, args):
        fname = args.get("fname")
        lname = args.get("lname")
        dao = UsersDAO()
        users_list = []
        if fname and lname:
            users_list = dao.getUsersByfNameAndlName(fname,lname)
        elif fname:
            users_list = dao.getUsersByfName(fname)
        elif lname:
            users_list = dao.getUsersBylName(lname)
        else:
            return jsonify(Error = "Not found"),404
        result_list = [
        for row in users_list:
            result = self.build_users_dict(row)
            result_list.append(Users = users_list)
