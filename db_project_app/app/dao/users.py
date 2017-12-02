from config.dbconfig import pg_config
import psycopg2
class UsersDAO:
   # def __init__(self):

    #    connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
    #    self.conn = psycopg2._connect(connection_url)

    def gettAllUsers(self):
        #cursor = self.conn.cursor()
        #query = "select * from parts;"
        #result = []
        #for row in cursor:
        #    result.append(row)
        return result

    def getUserById(self, uid):
        #cursor = self.conn.cursor()
        #query = "select * from users where uid = %s;"
        #cursor.execute(query, (pid,))
        #result = cursor.fetchone()
        return result


