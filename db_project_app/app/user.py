# Author: Genesis
from dao.users import UsersDAO
from handler.users import UsersHandler


class User:

    def __init__(self):
        self.uemail = None
        self.user_dict = None

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
