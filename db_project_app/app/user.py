# Author: Genesis
from dao.users import UsersDAO
from handler.users import UsersHandler


class User:

    def __init__(self):
        self.uid_var = None
        self.nid_var = None
        self.sid_var = None
        self.address_id = None
        self.phone_id = None
        self.location_id = None
        self.uemail = None
        self.sbusiness_type = None
        self.user_dict = {}

    def set_user(self, session_id):
        self.uemail = str(session_id)
        self.user_dict = self.get_dictionary()

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.uemail

    def is_admin(self):
        dao = UsersDAO()
        cursor = dao.connect_to_db()
        q = "Select * from appuser natural inner join appadmin where email = %s"
        cursor.execute(q, (self.uemail,))
        result = cursor.fetchone()
        if result:
            return True
        return False

    def is_supplier(self):
        dao = UsersDAO()
        cursor = dao.connect_to_db()
        q = "Select * from appuser natural inner join supplier where email = %s"
        cursor.execute(q, (self.uemail,))
        result = cursor.fetchone()
        if result:
            return True
        return False

    def get_dictionary(self):
        dao = UsersDAO()
        handler = UsersHandler()
        if self.is_admin():
            row = dao.getAdminByEmail(self.uemail)
            fdict = handler.build_admins_dict(row)
        elif self.is_supplier():
            row = dao.getSupplierByEmail(self.uemail)
            fdict = handler.build_supplier_dict(row)
        else:
            row = dao.getPInNeedByEmail(self.uemail)
            fdict = handler.build_person_in_need_dict(row)
        return fdict

    def uid(self):
        db_id = self.user_dict['uid']
        return str(db_id)

    def name(self):
        fname = str(self.user_dict['firstname'])
        lname = str(self.user_dict['lastname'])
        return fname + " " + lname

    def email(self):
        return self.uemail

    def phone(self):
        uphone = self.user_dict['phone']
        return str(uphone)

    def address(self):
        line1 = str(self.user_dict['line1'])
        line2 = str(self.user_dict['line2'])
        city = str(self.user_dict['city'])
        state = str(self.user_dict['state'])
        zipcode = str(self.user_dict['zipcode'])
        full_addr = line1 + ", " + line2 + ", " + city + ", " + state + ", " + zipcode
        return full_addr

    def business(self):
        sbusiness = self.user_dict['sbusiness_type']
        return str(sbusiness)

    def location(self):
        latitude = str(self.user_dict['latitude'])
        longitude = str(self.user_dict['longitud'])
        return latitude + ", " + longitude

# Needed for user_loader callback in views.py
    def get_user(self, session_id):
        handler = UsersHandler()
        result = handler.get_user(session_id)
        if result:
            usr = User()
            usr.set_user(session_id)
            return usr
        return None

# USER SIGN UP METHODS:
    def create_user(self, user_info_dict):
        dao = UsersDAO()
        cursor = dao.connect_to_db()

        # Appuser Table
        firstname = str(user_info_dict['first_name'])
        lastname = str(user_info_dict['last_name'])
        email = str(user_info_dict['email'])
        upassword = str(user_info_dict['psw'])
        q = "INSERT INTO appuser (firstname, lastname, email, upassword) VALUES (%s,%s,%s,%s);"
        cursor.execute(q, (firstname, lastname, email, upassword))
        q = "Select uid from appuser where email = %s"
        cursor.execute(q, (email,))
        result = cursor.fetchone()
        dao.commit_query()
        self.uid_var = str(result[0])

        # Phone Table:
        phone = str(user_info_dict['phone'])
        q = "INSERT INTO phone(uid, phone) VALUES (%s,%s);"
        cursor.execute(q, (self.uid_var, phone))
        q = "SELECT phone_id FROM phone NATURAL INNER JOIN appuser WHERE uid = %s"
        cursor.execute(q, (self.uid_var,))
        result = cursor.fetchone()
        dao.commit_query()
        self.phone_id = str(result[0])

        user_type = user_info_dict['user_type']  # 0 = person_in_need; 1 = supplier
        if user_type == str(0):
            q = "INSERT INTO person_in_need (uid) VALUES (%s);"
            cursor.execute(q, (self.uid_var,))
            q = "SELECT nid FROM person_in_need NATURAL INNER JOIN appuser WHERE uid = %s"
            cursor.execute(q, (self.uid_var,))
            result = cursor.fetchone()
            dao.commit_query()
            self.nid_var = str(result[0])
        else:
            self.sbusiness_type = user_info_dict['sbusiness_type']
            q = "INSERT INTO supplier (uid, sbusiness_type) VALUES (%s,%s);"
            cursor.execute(q, (self.uid_var,  self.sbusiness_type))
            q = "SELECT sid FROM supplier NATURAL INNER JOIN appuser WHERE uid = %s"
            cursor.execute(q, (self.uid_var,))
            result = cursor.fetchone()
            dao.commit_query()
            self.sid_var = str(result[0])

        # Address Table:
        line1 = str(user_info_dict['line1'])
        line2 = str(user_info_dict['line2'])
        city = str(user_info_dict['city'])
        state = str(user_info_dict['state'])
        zipcode = str(user_info_dict['zipcode'])
        if line2:
            q = "INSERT INTO address(uid, line1, line2, city, state, zipcode) VALUES (%s,%s,%s,%s,%s,%s);"
            cursor.execute(q, (self.uid_var, line1, line2, city, state, zipcode))
            dao.commit_query()
        else:
            q = "INSERT INTO address(uid, line1, city, state, zipcode) VALUES (%s,%s,%s,%s,%s);"
            cursor.execute(q, (self.uid_var, line1, city, state, zipcode))
        dao.commit_query()

        q = "SELECT address_id FROM address NATURAL INNER JOIN appuser WHERE uid = %s"
        cursor.execute(q, (self.uid_var,))
        result = cursor.fetchone()
        dao.commit_query()
        self.address_id = str(result[0])

        # Location Table (Same location for everyone for now):
        q = "INSERT INTO user_location(uid, latitude, longitud) VALUES(%s, 18.171690, -66.977021);"
        cursor.execute(q, (self.uid_var,))
        dao.commit_query()

        q = "SELECT address_id FROM address NATURAL INNER JOIN appuser WHERE uid = %s"
        cursor.execute(q, (self.uid_var,))
        result = cursor.fetchone()
        dao.commit_query()
        self.address_id = str(result[0])

    def set_new_user(self, usr_parameters):
        usr_type = usr_parameters['user_type']
        self.uemail = usr_parameters['email']

        # PERSON IN NEED DICTIONARY
        if usr_type == str(0):
            self.user_dict['uid'] = self.uid_var
            self.user_dict['firstname'] = str(usr_parameters['first_name'])
            self.user_dict['lastname'] = str(usr_parameters['last_name'])
            self.user_dict['email'] = str(usr_parameters['email'])
            self.user_dict['upassword'] = str(usr_parameters['psw'])
            self.user_dict['nid'] = self.nid_var
            self.user_dict['address_id'] = self.address_id
            self.user_dict['line1'] = str(usr_parameters['line1'])
            self.user_dict['line2'] = str(usr_parameters['line2'])
            line2 = usr_parameters['line2']
            if not line2:
                self.user_dict['line2'] = ""
            self.user_dict['city'] = str(usr_parameters['city'])
            self.user_dict['state'] = str(usr_parameters['state'])
            self.user_dict['zipcode'] = str(usr_parameters['zipcode'])
            self.user_dict['location_id'] = self.location_id
            self.user_dict['latitude'] = "18.171690"
            self.user_dict['longitud'] = "-66.977021"
            self.user_dict['phone_id'] = self.phone_id
            self.user_dict['phone'] = str(usr_parameters['phone'])

        # SUPPLIER DICTIONARY
        else:
            self.user_dict['uid'] = self.uid_var
            self.user_dict['firstname'] = str(usr_parameters['first_name'])
            self.user_dict['lastname'] = str(usr_parameters['last_name'])
            self.user_dict['email'] = str(usr_parameters['email'])
            self.user_dict['upassword'] = str(usr_parameters['psw'])
            self.user_dict['sid'] = self.sid_var
            self.user_dict['sbusiness_type'] = str(usr_parameters['sbusiness_type'])
            self.user_dict['address_id'] = self.address_id
            self.user_dict['line1'] = str(usr_parameters['line1'])
            self.user_dict['line2'] = str(usr_parameters['line2'])
            line2 = str(usr_parameters['line2'])
            if not line2:
                self.user_dict['line2'] = ""
            self.user_dict['city'] = str(usr_parameters['city'])
            self.user_dict['state'] = str(usr_parameters['state'])
            self.user_dict['zipcode'] = str(usr_parameters['zipcode'])
            self.user_dict['location_id'] = self.location_id
            self.user_dict['latitude'] = "18.171690"
            self.user_dict['longitud'] = "-66.977021"
            self.user_dict['phone_id'] = self.phone_id
            self.user_dict['phone'] = str(usr_parameters['phone'])
