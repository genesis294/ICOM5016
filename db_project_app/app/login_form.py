# Author: Genesis
from dao.users import UsersDAO


class LoginForm:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_user(self):
        dao = UsersDAO()
        return dao.getUserByEmailAndPassword(self.email, self.password)
