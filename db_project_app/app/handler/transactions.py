# Author: Genesis

from flask import jsonify
from dao.transactions import TransactionsDAO


class TransactionsHandler:

    # Builds the transactions dictionary for transactions made by a person in need.
    def build_transactions_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['tid'] = row[3]
        result['cid'] = row[4]
        result['ttotal_cost'] = row[5]
        result['tdate_time'] = row[6]
        result['cardnumber'] = row[7]
        result['exp_date'] = row[8]
        result['cvv'] = row[9]
        result['card_type'] = row[10]
        result['cardholder'] = row[11]
        return result

    # Builds the transactions dictionary for transactions supplied by a supplier.
    def build_supplier_transactions_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sbusiness_type'] = row[1]
        result['firstname'] = row[2]
        result['lastname'] = row[3]
        result['tid'] = row[4]
        result['tdate_time'] = row[5]
        result['nid'] = row[6]
        result['ciamount'] = row[7]
        result['ciprice'] = row[8]
        result['rname'] = row[9]
        result['rcategory'] = row[10]
        return result

    def getAllTransactions(self):
        dao = TransactionsDAO()
        transaction_list = dao.getAllTransactions()
        result_list = []
        for row in transaction_list:
            result = self.build_transactions_dict(row)
            result_list.append(result)
        return jsonify(Transactions = result_list)

    def getTransactionByID(self, tid):
        dao = TransactionsDAO()
        t = dao.getTransactionByID(tid)
        if not t:
            return jsonify(Error = "Transaction Not Found."), 404
        else:
            transaction = self.build_transactions_dict(t)
            return jsonify(Transaction = transaction)

    def getTransactionsByUserID(self, uid):
        dao = TransactionsDAO()
        transaction_list = dao.getTransactionsByUserID(uid)
        if not transaction_list:
            return jsonify(Error = "Transactions Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transactions_dict(row)
                result_list.append(result)
            return jsonify(User_Transactions = result_list)

    def getTransactionsByCartID(self, cid):
        dao = TransactionsDAO()
        transaction_list = dao.getTransactionsByCartID(cid)
        if not transaction_list:
            return jsonify(Error = "Transactions Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transactions_dict(row)
                result_list.append(result)
            return jsonify(Transactions=result_list)

    def getTransactionsByUserEmail(self, email):
        dao = TransactionsDAO()
        transaction_list = dao.getTransactionsByUserEmail(email)
        if not transaction_list:
            return jsonify(Error = "Transactions Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transactions_dict(row)
                result_list.append(result)
            return jsonify(Transactions=result_list)

    def getAllSuppliedTransactions(self):
        dao = TransactionsDAO()
        transaction_list = dao.getAllSuppliedTransactions()
        result_list = []
        for row in transaction_list:
            result = self.build_supplier_transactions_dict(row)
            result_list.append(result)
        return jsonify(Supplied_Transactions = result_list)

    def getTransactionsBySupplierID(self, sid):
        dao = TransactionsDAO()
        transaction_list = dao.getTransactionsBySupplierID(sid)
        if not transaction_list:
            return jsonify(Error = "Transactions Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_supplier_transactions_dict(row)
                result_list.append(result)
            return jsonify(Transactions=result_list)

    def searchTransactions(self, args):
        dao = TransactionsDAO()

        date = args.get("date")

        if date:
            transaction_list = dao.getTransactionsByDate(date)
        else:
            return jsonify(Error = "Malformed query string"), 400

        result_list = []
        for row in transaction_list:
            result = self.build_transactions_dict(row)
            result_list.append(result)

        return jsonify(Transactions = result_list)