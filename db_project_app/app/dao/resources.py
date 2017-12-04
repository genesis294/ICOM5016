#from config.dbconfig import pg_config
import psycopg2

# List of stuff donated
donations = [{'rid': 9, 'rname': 'water', 'rquantity': 100, 'rprice': 0, "sid": 3, "date_added": "30/10/17"},
             {'rid': 10, 'rname': 'water', 'rquantity': 800, 'rprice': 0, "sid": 5, "date_added": "30/10/17"},
             {'rid': 3, 'rname': 'military food', 'rquantity': 458, 'rprice': 0, "sid": 6, "date_added": "31/10/17"},
             {'rid': 12, 'rname': 'clothes', 'rquantity': 223, 'rprice': 0, "sid": 7, "date_added": "30/10/17"}]

# List of stuff being requested
requests = [{'rid': 1, 'rname': 'water', 'rquantity': 100, "sid": 1, "date_added": "30/10/17"},
            {'rid': 4, 'rname': 'gasoline', 'rquantity': 800, "sid": 0, "date_added": "31/10/17"},
            {'rid': 5, 'rname': 'clothes', 'rquantity': 1, "sid": 4, "date_added": "30/10/17"},
            {'rid': 7, 'rname': 'canned food', 'rquantity': 20, "sid": 4, "date_added": "31/10/17"},
            {'rid': 13, 'rname': 'water', 'rquantity': 100, "sid": 10, "date_added": "1/11/17"},
            {'rid': 14, 'rname': 'water', 'rquantity': 800, "sid": 11, "date_added": "3/11/17"},
            {'rid': 15, 'rname': 'ice', 'rquantity': 156, "sid": 40, "date_added": "1/1/17"},
            {'rid': 17, 'rname': 'canned food', 'rquantity': 20, "sid": 44, "date_added": "31/10/17"}]

# List of stuff available for sale
supplies = [{'rid': 2, 'rname': 'water', 'rquantity': 250, 'rprice': 3.50, "sid": 3, "date_added": "30/10/17"},
            {'rid': 11, 'rname': 'gasoline', 'rquantity': 1000, 'rprice': 0.99, "sid": 2, "date_added": "30/10/17"},
            {'rid': 6, 'rname': 'gandules', 'rquantity': 200, 'rprice': 1.20, "sid": 5, "date_added": "30/10/17"},
            {'rid': 8, 'rname': 'water', 'rquantity': 789, 'rprice': 3.67, "sid": 5, "date_added": "31/10/17"},
            {'rid': 16, 'rname': 'ice', 'rquantity': 200, 'rprice': 4, "sid": 35, "date_added": "1/11/17"}]

# Everything that is available to the user
available = []
available.extend(supplies)
available.extend(donations)

# All resources
resources = []
resources.extend(requests)
resources.extend(donations)
resources.extend(supplies)


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
            if row["rname"] == name and row["rquantity"] >= int(quantity):
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

    def getRequestByQuantity(self, quantity):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rquantity <= %s;"
        # cursor.execute(query, (price, ))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in requests:
            if row["rquantity"] >= int(quantity):
                result.append(row)
        return result

    ##################################################
    #           Available resources methods          #
    ##################################################
    # Get the resources available for buying
    def getAllAvailable(self):
        return available
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
        for row in available:
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
        for row in available:
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
        for row in available:
            if row["rname"] == name and row["rquantity"] >= int(quantity) \
                    and row["rprice"] <= float(price):
                result.append(row)
        return result

    # Get available by name and price
    def getAvailableByNamePrice(self, name, price):
        # cursor = self.conn.cursor()
        # query = "select * from available where rname = %s, rprice <= %s;"
        # cursor.execute(query, (name, price))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in available:
            if row["rname"] == name and row["rprice"] <= float(price):
                result.append(row)
        return result

    # Get available by name and quantity
    def getAvailableByNameQuantity(self, name, quantity):
        # cursor = self.conn.cursor()
        # query = "select * from available where rname = %s, rquantity >= %s;"
        # cursor.execute(query, (name, quantity))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in available:
            if row["rname"] == name and row["rquantity"] >= int(quantity):
                result.append(row)
        return result

    # Get available based on price
    def getAvailableByPrice(self, price):
        # cursor = self.conn.cursor()
        # query = "select * from available where rprice <= %s;"
        # cursor.execute(query, (price, ))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in available:
            if row["rprice"] <= float(price):
                result.append(row)
        return result

    def getAvailableByQuantity(self, quantity):
        # cursor = self.conn.cursor()
        # query = "select * from requests where rquantity <= %s;"
        # cursor.execute(query, (price, ))
        # result = []
        # for row in cursor:
        #    result.append(row)
        # return result
        result = []
        for row in available:
            if row["rquantity"] >= int(quantity):
                result.append(row)
        return result

    ##################################################
    #           Statistics methods                   #
    ##################################################

    # Get stats of the day
    def getDailyStats(self):
        results = {}
        results['all'] = len(resources)
        results['requests'] = len(requests)
        results['available'] = len(available)
        results['supplies'] = len(supplies)
        results['donated'] = len(donations)

        match = 0

        for resource in requests:
            for supply in available:
                    if resource['rname'] == supply['rname'] and supply['rquantity'] >= resource['rquantity']:
                        match += 1

        results['matches'] = match

        return results

    # Get stats of the week
    def getWeeklyStats(self):
        return self.getDailyStats()

    # Get stats of the regions
    # Eight senatorial districts:
    # San Juan, Bayamon, Arecibo, Mayaguez, Ponce, Guayama, Humacao, Carolina
    def getRegionalStats(self):
        results = {}
        # Districts: [req, ava, don]
        results['sanjuan'] = [3, 4, 2]
        results['bayamon'] = [0, 2, 1]
        results['arecibo'] = [1, 0, 0]
        results['mayaguez'] = [2, 2, 1]
        results['ponce'] = [0, 0, 0]
        results['guayama'] = [0, 0, 0]
        results['humacao'] = [1, 1, 0]
        results['carolina'] = [1, 0, 0]
        return results



