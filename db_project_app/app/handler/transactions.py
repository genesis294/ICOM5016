# Author: Genesis

from flask import jsonify
from dao.transactions import TransactionsDAO


class TransactionsHandler:

    #Builds the transactions dictionary.
    def build_transactions_dict(self, row):
        result = {}
        result['tid'] = row['tid']
        result['uid'] = row['uid']
        result['cid'] = row['cid']
        result['payment_method'] = row['payment_method']
        result['total_cost'] = row['total_cost']
        result['quantity'] = row['quantity']
        result['date_of_purchase'] = row['date_of_purchase']
        return result


    def getAllTransactions(self):
        dao = TransactionsDAO()
        transaction_list = dao.getAllTransactions()
        result_list = []
        for row in transaction_list:
            result = self.build_transactions_dict(row)
            result_list.append(result)
        return jsonify(Transactions = result_list)

    def getTransactionByID(self):
        dao = TransactionsDAO()
        t = dao.getTransactionByID()
        if not t:
            return jsonify(Error = "Transaction Not Found."), 404
        else:
            transaction = self.build_transactions_dict(t)
            return jsonify(Transaction = transaction)

    def getTransactionsByUserID(self):
        dao = TransactionsDAO()
        transaction_list = dao.getTransactionsByUserID()
        if not transaction_list:
            return jsonify(Error = "Transactions Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transactions_dict(row)
                result_list.append(result)
            return jsonify(User_Transactions = result_list)

    def getTransactionsByCartID(self):
        dao = TransactionsDAO()
        transaction_list = dao.getTransactionsByCartID()
        if not transaction_list:
            return jsonify(Error = "Transactions Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transactions_dict(row)
                result_list.append(result)
            return jsonify(Transactions=result_list)

    def searchTransactions(self, args):
        dao = TransactionsDAO()
        payment_method = args.get("payments_method")
        date = args.get("date_of_purchase")
        transaction_list = []

        if payment_method:
            transaction_list = dao.getTransactionsByPaymentMethod(payment_method)
        elif date:
            transaction_list = dao.getTransactionsByDate(date)
        else:
            return jsonify(Error = "Malformed query string"), 400

        result_list = []
        for row in transaction_list:
            result = self.build_transactions_dict(row)
            result_list.append(result)

        return jsonify(Transactions = result_list)