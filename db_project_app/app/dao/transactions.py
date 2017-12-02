# Author: Genesis

from config.dbconfig import pg_config
import psycopg2

# List of test transactions to be used in first phase of the project, before the db can be accessed
TRANSACTION_LIST = [{"tid": 1, "uid": 3, "cid": 4, "payment_method": "Credit Card", "total_cost": 50.00,
                     "quantity": 1, "date_of_purchase": "25/10/17"},

                    {"tid": 2, "uid": 5, "cid": 9, "payment_method": "Credit Card", "total_cost": 250.00,
                     "quantity": 6, "date_of_purchase": "25/10/17"},

                    {"tid": 3, "uid": 15, "cid": 6, "payment_method": "PayPal", "total_cost": 86.00,
                     "quantity": 4, "date_of_purchase": "26/10/17"},

                    {"tid": 4, "uid": 3, "cid": 10, "payment_method": "ATH Movil", "total_cost": 150.00,
                     "quantity": 10, "date_of_purchase": "29/10/17"},

                    {"tid": 5, "uid": 1, "cid": 13, "payment_method": "Credit Card", "total_cost": 10.00,
                     "quantity": 1, "date_of_purchase": "29/10/17"},

                    {"tid": 6, "uid": 9, "cid": 14, "payment_method": "Credit Card", "total_cost": 13.00,
                     "quantity": 3, "date_of_purchase": "30/10/17"},

                    {"tid": 7, "uid": 8, "cid": 17, "payment_method": "PayPal", "total_cost": 9.00,
                     "quantity": 2, "date_of_purchase": "30/10/17"},

                    {"tid": 8, "uid": 5, "cid": 18, "payment_method": "PayPal", "total_cost": 50.00,
                     "quantity": 1, "date_of_purchase": "30/10/17"},

                    {"tid": 9, "uid": 2, "cid": 20, "payment_method": "Credit Card", "total_cost": 140.00,
                     "quantity": 17, "date_of_purchase": "3/11/17"},

                    {"tid": 10, "uid": 6, "cid": 6, "payment_method": "ATH Movil", "total_cost": 99.00,
                     "quantity": 7, "date_of_purchase": "4/11/17"}]


class TransactionsDAO:

    #Initialization method
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # Returns a list of all transactions.
    def getAllTransactions(self):
        return TRANSACTION_LIST

    # Get transactions by their ID. Returns a list with the transaction if it exists; returns None otherwise.
    def getTransactionByID(self, tid):
        for row in TRANSACTION_LIST:
            if row["tid"] == tid:
                return row
        return None

    # Get transactions by their User ID.
    def getTransactionsByUserID(self, uid):
        transactions = []
        for row in TRANSACTION_LIST:
            if row["uid"] == uid:
                transactions.append(row)
        return transactions

    # Get transactions by their Cart ID.
    def getTransactionsByCartID(self, cid):
        transactions = []
        for row in TRANSACTION_LIST:
            if row["cid"] == cid:
                transactions.append(row)
        return transactions

    # Get transactions by Payment Method
    def getTransactionsByPaymentMethod(self, payment_method):
        transactions = []
        for row in TRANSACTION_LIST:
            if row["payments_method"] == payment_method:
                transactions.append(row)
        return transactions

    # Get transactions by Date of Purchase
    def getTransactionsByDate(self, date):
        transactions = []
        for row in TRANSACTION_LIST:
            if row["date_of_purchase"] == date:
                transactions.append(row)
        return transactions



