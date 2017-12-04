#from config.dbconfig import pg_config
#import psycopg2

Users_List = [{'uid': 1, 'fname': 'Juan', 'lname': 'Ruiz', 'email': 'juanruiz3@gmail.com',
                   'phone': '787-743-4439','password': 'soyloco123'},

              {'uid': 2, 'fname': 'Rosa', 'lname': 'Rivera', 'email': 'rrosa@gmail.com',
                   'phone': '939-234-9832','password': 'redrose3'},

              {'uid': 3, 'fname': 'Pedro', 'lname': 'De Las Piedras', 'email': 'pedrito94@gmail.com',
                   'phone': '787-000-8192','password': 'pedrodelaspiedras'},

              {'uid': 4, 'fname': 'Carlos', 'lname': 'Colon', 'email': 'carloscolon3rd@gmail.com',
                   'phone': '787-673-4834','password': '3CColon12'},

              {'uid': 5, 'fname': 'Tatiana', 'lname': 'Gomez', 'email': 'tatig@gmail.com',
                   'phone': '939-453-9876','password': 'lababy83'},

              {'uid': 6, 'fname': 'Jerry', 'lname': 'Torres', 'email': 'jerrytorres@hotmail.com',
                   'phone': '787-943-8010','password': 'jerry123'},

              {'uid': 7, 'fname': 'Pedro', 'lname': 'Lopez', 'email': 'pLopez@gmail.com',
                   'phone': '939-748-2013','password': 'PlanetEarth'},

              {'uid': 8, 'fname': 'Tito', 'lname': 'Rivera', 'email': 'titorivera@upr.edu',
                   'phone': '787-098-7548','password': 'BB1439'},

              {'uid': 9, 'fname': 'Anthony', 'lname': 'Rivera', 'email': 'antrivera@gmail.com',
                   'phone': '787-091-3572','password': '1234567'},

              {'uid': 10, 'fname': 'Tito', 'lname': 'Mendez', 'email': 'titomendez@gmail.com',
                   'phone': '939-404-9988','password': 'titoelloquillo'},

              {'uid': 11, 'fname': 'Thalia', 'lname': 'Gonzalez', 'email': 'thalia34@gmail.com',
                   'phone': '787-673-4932','password': 'thalialabest'},

              {'uid': 12, 'fname': 'Wilfredo', 'lname': 'Estevez', 'email': 'westevez@hotmail.com',
                   'phone': '787-453-8362','password': 'gasstation'},

              {'uid': 13, 'fname': 'Milagros', 'lname': 'Ruiz', 'email': 'milagrosrr@gmail.com',
                   'phone': '939-345-4567','password': 'milagros123'},

              {'uid': 14, 'fname': 'Bebo', 'lname': 'Cuevas', 'email': 'BeboCuevas45@outlook.com',
                   'phone': '787-485-4543','password': 'MiCarro'},

              {'uid': 15, 'fname': 'Marie', 'lname': 'Clark', 'email': 'marieck2@gmail.com',
                   'phone': '787-990-3456','password': 'marie4ee'},

              {'uid': 16, 'fname': 'Carlitos', 'lname': 'Cruz', 'email': 'cruzCarlitos@hotmail.com',
                   'phone': '939-666-8753','password': 'cruzcruz'}]

#AdmiList = [{'uid': 1 ,'aid' : 1}]

#Users_List.extend(AdmiList)

class UsersDAO:

    def getAllUsers(self):
        return Users_List

    def getUsersById(self, uid):
        for row in Users_List:
            if row["uid"] == uid:
                return row
        return None

    def getUsersByfNameAndlName(self, fname, lname):
        users = []
        for row in Users_List:
            if row['fname'] == fname and row['lname'] == lname:
                users.append(row)
        return users

    def getUsersByfName(self, fname):
        users = []
        for row in Users_List:
            if row["fname"] == fname:
                users.append(row)
        return users

    def getUsersBylName(self, lname):
        users = []
        for row in Users_List:
            if row['lname'] == lname:
                users.append(row)
        return users


# Method to get a user by their email address. (Added by Genesis. Need it for login)
    def getUserByEmail(self, email):
        for row in Users_List:
            if row["email"] == email:
                return row
        return None