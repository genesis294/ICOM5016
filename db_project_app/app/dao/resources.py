#from config.dbconfig import pg_config
import psycopg2

requests = [{'rid': 1, 'rname': 'water', 'rquantity': 100, 'rprice': 5.00, "sid": 1},
            {'rid': 4, 'rname': 'gasoline', 'rquantity': 800, 'rprice': 1.00, "sid": 0},
            {'rid': 5, 'rname': 'clothes', 'rquantity': 1, 'rprice': 10.00, "sid": 4},
            {'rid': 7, 'rname': 'ravioli', 'rquantity': 20, 'rprice': 0.75, "sid": 4}]

supplies = [{'rid': 2, 'rname': 'water', 'rquantity': 250, 'rprice': 3.50, "sid": 3},
            {'rid': 3, 'rname': 'gas-Puma', 'rquantity': 1000, 'rprice': 0.99, "sid": 2},
            {'rid': 6, 'rname': 'gandules', 'rquantity': 200, 'rprice': 1.20, "sid": 5},
            {'rid': 8, 'rname': 'water', 'rquantity': 789, 'rprice': 3.67, "sid": 5}]


class ResourcesDAO:
    ##################################################
    #           Requested resources methods          #
    ##################################################
    # Returns all the rquests in the database
    def getAllRequests(self):
        return requests
        #cursor = self.conn.cursor()
        #query = "select * from requests;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        #return result

    # Get a request by its id
    def getRequestResourceById(self, rid):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rid = %s;"
        # cursor.execute(query, (pid,))
        # result = cursor.fetchone()
        # return result
        for row in requests:
            if row['rid'] == rid:
                return row
        return None

    # Get request by name
    def getRequestByName(self, name):
        #cursor = self.conn.cursor()
        #query = "select * from available where rname = %s;"
        #cursor.execute(query, (color,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        #return result
        result = []
        for row in requests:
            if row["rname"] == name:
                result.append(row)
        return result

    # Get request by name, quantity and price
    def getRequestByNameQuantityPrice(self, name, quantity, price):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rname = %s, rquantity >= %s, rprice <= %s;"
        # cursor.execute(query, (name, quantity, price))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in requests:
            if row["rname"] == name and row["rquantity"] >= int(quantity) \
                    and row["rprice"] <= float(price):
                result.append(row)
        return result

    # Get request by name and price
    def getRequestByNamePrice(self, name, price):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rname = %s, rprice <= %s;"
        # cursor.execute(query, (name, price))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in requests:
            if row["rname"] == name and row["rprice"] <= float(price):
                result.append(row)
        return result

    # Get request by name and quantity
    def getRequestByNameQuantity(self, name, quantity):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rname = %s, rquantity >= %s;"
        # cursor.execute(query, (name, quantity))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in requests:
            if row["rname"] == name and row["rquantity"] <= int(quantity):
                result.append(row)
        return result

    # Get requests based on price
    def getRequestByPrice(self, price):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rprice <= %s;"
        # cursor.execute(query, (price, ))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in requests:
            if row["rprice"] <= float(price):
                result.append(row)
        return result

    ##################################################
    #           Available resources methods          #
    ##################################################
    # Get the resources available for buying
    def getAllAvailable(self):
        return supplies
        #cursor = self.conn.cursor()
        #query = "select * from available;"
        #cursor.execute(query)
        #result = []
        #for row in cursor:
        #    result.append(row)
        #return result

    # Get available resources by id
    def getAvailableResourceById(self, rid):
        # cursor = self.conn.cursor()
        # query = "select * from available where rid = %s;"
        # cursor.execute(query, (pid,))
        # result = cursor.fetchone()
        # return result
        for row in supplies:
            if row['rid'] == rid:
                return row
        return None

    # Get available resources by name
    def getAvailableByName(self, name):
        #cursor = self.conn.cursor()
        #query = "select * from available where rname = %s;"
        #cursor.execute(query, (color,))
        #result = []
        #for row in cursor:
        #    result.append(row)
        #return result
        result = []
        for row in supplies:
            if row["rname"] == name:
                result.append(row)
        return result

    # Get available by name, quantity and price
    def getAvailableByNameQuantityPrice(self, name, quantity, price):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rname = %s, rquantity >= %s, rprice <= %s;"
        # cursor.execute(query, (name, quantity, price))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in requests:
            if row["rname"] == name and row["rquantity"] >= int(quantity) \
                    and row["rprice"] <= float(price):
                result.append(row)
        return result

    # Get available by name and price
    def getAvailableByNamePrice(self, name, price):
        # cursor = self.conn.cursor()
        # query = "select * from supplies where rname = %s, rprice <= %s;"
        # cursor.execute(query, (name, price))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in supplies:
            if row["rname"] == name and row["rprice"] <= float(price):
                result.append(row)
        return result

    # Get available by name and quantity
    def getAvailableByNameQuantity(self, name, quantity):
        # cursor = self.conn.cursor()
        # query = "select * from supplies where rname = %s, rquantity >= %s;"
        # cursor.execute(query, (name, quantity))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in supplies:
            if row["rname"] == name and row["rquantity"] <= int(quantity):
                result.append(row)
        return result

    # Get available based on price
    def getAvailableByPrice(self, price):
        # cursor = self.conn.cursor()
        # query = "select * from supplies where rprice <= %s;"
        # cursor.execute(query, (price, ))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in supplies:
            if row["rprice"] <= float(price):
                result.append(row)
        return result



