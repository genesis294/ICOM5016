# Author: Genesis
from dao.users import UsersDAO


class LoginForm:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_user(self):
        dao = UsersDAO()
        return dao.getUserByEmailAndPassword(self.email, self.password)

class SignUpForm:
    def __init__(self, parameter_dict):
        self.email = parameter_dict['email']
        self.psw = parameter_dict['psw']
        self.psw_repeat = parameter_dict['psw-repeat']

    def is_existing_user(self):
        dao = UsersDAO()
        return dao.getUserByEmail(self.email)

    def passwords_match(self):
        if self.psw == self.psw_repeat:
            return True
        return False

