from config.db_config import pg_config
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

# TODO
    def getUsersByfNameAndlName(self, fname, lname):
        pass

# TODO
    def getUsersByfName(self, fname):
        pass

# TODO
    def getUsersBylName(self, lname):
        pass

# TODO
    def getUserByEmail(self, email):
        pass

# Queries to get admins
    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join appadmin;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminById(self, aid):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join appadmin where aid = %s"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result

# Queries to get suppliers
    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersBySID(self, sid):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join supplier where sid = %s"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

# TODO
    def getBusiness(self, TBusiness):
        pass

# Queries to get persons in need
    def getAllPInNeed(self):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join person_in_need;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPInNeedByNID(self,nid):
        cursor = self.conn.cursor()
        query = "select * from appuser natural inner join person_in_need where nid = %s"
        cursor.execute(query, (nid,))
        result = cursor.fetchone()
        return result