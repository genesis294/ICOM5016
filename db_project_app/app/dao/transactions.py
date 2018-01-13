# Author: Genesis

from config.dbconfig import pg_config
import psycopg2


class TransactionsDAO:

    # Initialization method
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=localhost port=5432" % \
                         (pg_config['dbname'],
                          pg_config['user'],
                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # Returns a list of all transactions made by all users.
    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, tid, cid, ttotal_cost, tdate_time, " \
                "cardnumber, exp_date, cvv, card_type, cardholder " \
                "from cart natural inner join transactions natural inner join person_in_need " \
                "natural inner join appuser natural inner join pays natural inner join credit_card;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transactions by their ID
    def getTransactionByID(self, tid):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, tid, cid, ttotal_cost, tdate_time, " \
                "cardnumber, exp_date, cvv, card_type, cardholder " \
                "from cart natural inner join transactions natural inner join person_in_need " \
                "natural inner join appuser natural inner join pays natural inner join credit_card " \
                "where tid = %s;"
        cursor.execute(query, (tid,))
        result = cursor.fetchone()
        return result

    # Get transactions by their User ID.
    def getTransactionsByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, tid, cid, ttotal_cost, tdate_time, " \
                "cardnumber, exp_date, cvv, card_type, cardholder " \
                "from cart natural inner join transactions natural inner join person_in_need " \
                "natural inner join appuser natural inner join pays natural inner join credit_card " \
                "where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transactions by their Cart ID.
    def getTransactionsByCartID(self, cid):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, tid, cid, ttotal_cost, tdate_time, " \
                "cardnumber, exp_date, cvv, card_type, cardholder " \
                "from cart natural inner join transactions natural inner join person_in_need " \
                "natural inner join appuser natural inner join pays natural inner join credit_card " \
                "where cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transactions by Date of Purchase
    def getTransactionsByDate(self, date):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, tid, cid, ttotal_cost, tdate_time, " \
                "cardnumber, exp_date, cvv, card_type, cardholder " \
                "from cart natural inner join transactions natural inner join person_in_need " \
                "natural inner join appuser natural inner join pays natural inner join credit_card " \
                "where tdate_time = %s;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get all transactions supplied by suppliers
    def getAllSuppliedTransactions(self):
        cursor = self.conn.cursor()
        query = "select sid,sbusiness_type,firstname,lastname,tid,tdate_time,nid,ciamount,ciprice,rname,rcategory " \
                "from transactions natural inner join cart natural inner join cart_item natural inner join item_list " \
                "natural inner join supplier natural inner join appuser natural inner join resources"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transactions by Supplier ID
    def getTransactionsBySupplierID(self, sid):
        cursor = self.conn.cursor()
        query = "select sid,sbusiness_type,firstname,lastname,tid,tdate_time,nid,ciamount,ciprice,rname,rcategory " \
                "from transactions natural inner join cart natural inner join cart_item natural inner join item_list " \
                "natural inner join supplier natural inner join appuser natural inner join resources " \
                "where sid = %s"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get transactions by User email
    def getTransactionsByUserEmail(self, email):
        cursor = self.conn.cursor()
        query = "select uid, firstname, lastname, tid, cid, ttotal_cost, tdate_time, " \
                "cardnumber, exp_date, cvv, card_type, cardholder " \
                "from cart natural inner join transactions natural inner join person_in_need " \
                "natural inner join appuser natural inner join pays natural inner join credit_card " \
                "where email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result



