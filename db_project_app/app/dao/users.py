from config.dbconfig import pg_config
import psycopg2


class UsersDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

# Queries to get general users
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from appuser;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from appuser where uid = %s"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUsersByfNameAndlName(self, fname, lname):
        cursor = self.conn.cursor()
        query = "select * from appuser where firstname = %s and lastname = %s"
        cursor.execute(query, (fname, lname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByfName(self, fname):
        cursor = self.conn.cursor()
        query = "select * from appuser where firstname = %s"
        cursor.execute(query, (fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersBylName(self, lname):
        cursor = self.conn.cursor()
        query = "select * from appuser where lastname = %s"
        cursor.execute(query, (lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * from appuser where email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def getUserByEmailAndPassword(self, email, password):
        cursor = self.conn.cursor()
        query = "select * from appuser where email = %s and upassword = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        return result

# Queries to get admins
    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join appadmin natural inner join phone;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminById(self, aid):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join appadmin natural inner join " \
                "phone where aid = %s"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result

    def getAdminByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join appadmin natural inner join " \
                "phone where email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

# Queries to get suppliers
    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from appuser natural inner join supplier natural inner join address " \
                "natural inner join user_location natural inner join phone"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersBySID(self, sid):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join supplier natural inner join address " \
                "natural inner join user_location natural inner join phone "\
                "where sid = %s"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getSupplierByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join supplier natural inner join address " \
                "natural inner join user_location natural inner join phone "\
                "where email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    #Get Suppliers by City Only
    def getSuppliersByCity(self, city):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join supplier " \
                "natural inner join address natural inner join user_location natural inner join phone " \
                "where city =%s"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBusiness(self, TBusiness):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join supplier " \
                "natural inner join address natural inner join user_location natural inner join phone " \
                "where sbusiness_type = %s"
        cursor.execute(query, (TBusiness,))
        result = cursor.fetchone()
        return result

# Queries to get persons in need
    def getAllPInNeed(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from appuser natural inner join person_in_need natural inner join address " \
                "natural inner join user_location natural inner join phone;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPInNeedByNID(self,nid):
        cursor = self.conn.cursor()
        query = "select * " \
                "from appuser natural inner join person_in_need natural inner join address " \
                "natural inner join user_location natural inner join phone " \
                "where nid = %s;"
        cursor.execute(query, (nid,))
        result = cursor.fetchone()
        return result

    def getPInNeedByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * " \
                "from appuser natural inner join person_in_need natural inner join address " \
                "natural inner join user_location natural inner join phone " \
                "where email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

# Method used in User() class in user.py
# Needed for log in functionality
    def connect_to_db(self):
        cursor = self.conn.cursor()
        return cursor
