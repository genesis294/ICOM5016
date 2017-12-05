# Author: Genesis

# from dao.users import UsersDAO


class User:

    def __init__(self, usr_dict):
        self.user_dict = usr_dict

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
        return str(self.user_dict["uid"])

    def name(self):
        return str(self.user_dict["fname"])

    def isAdmin(self):
        pass

    def isSUpplier(self):
        pass


# Meant to be used with user_handler callback in views.py
#     def getUser(self, uid):
#         if uid == self.get_id():
#             return self
#         else:
#             return None