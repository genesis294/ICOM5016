# Author: Genesis
from handler.users import UsersDAO


class LoginForm:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    # returns: None if user does not exist or if the password is incorrect; the user dictionary otherwise.
    def validate_on_submit(self):
        usr = UsersDAO().getUserByEmail(self.email)
        if not usr or usr["password"] != self.password:
            return None
        else:
            return usr




