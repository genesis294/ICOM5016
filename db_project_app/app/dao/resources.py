from psycopg2._psycopg import AsIs

from config.db_config import pg_config
from operator import itemgetter
import datetime
import psycopg2


class ResourcesDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=localhost port=5432" % \
                         (pg_config['dbname'],
                          pg_config['user'],
                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    ##################################################
    #   Methods that apply to resources in general   #
    ##################################################
    # Get all resources in resource table
    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Inserts a resource and returns its id.
    def insert(self, name, quantity, category):
        cursor = self.conn.cursor()
        query = "insert into resources(rname, rquantity, rdate_added, rcategory) " \
                "values (%s, %s, %s, %s) returning rid;"
        # Gets current date
        now = datetime.datetime.now()
        # Saves current date in english format
        date_added = now.strftime("%d-%m-%Y")
        cursor.execute(query, (name, quantity, date_added, category,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    # Get general resource info by id
    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    # Insert resource specific
    def insertSpecificResource(self, rid, category, form):
        # We can now insert in resource specific table
        # category will indicate in which table we can add the supply
        cursor = self.conn.cursor()
        # If resource is water
        if category == "water":
            wtype = form['wtype']
            brand = form['wbrand']
            query = "insert into water(rid, wtype, wbrand) " \
                    "values (%s, %s, %s) returning rid;"
            cursor.execute(query, (rid, wtype, brand,))
        # Ice
        elif category == "ice":
            size = form['isize']
            query = "insert into ice(rid, isize) " \
                    "values (%s, %s) returning rid;"
            cursor.execute(query, (rid, size,))
        # Food
        elif category == "food":
            ftype = form['ftype']
            brand = form['fbrand']
            amount = form['famount']
            exp_date = form['fexp_date']
            query = "insert into food(rid, ftype, fbrand, famount, fexp_date) " \
                    "values (%s, %s, %s, %s, %s) returning rid;"
            cursor.execute(query, (rid, ftype, brand, amount, exp_date))
        # Medication
        elif category == "medication":
            mtype = form['mtype']
            amount = form['mamount']
            dose = form['mdose']
            brand = form['mbrand']

            query = "insert into medication(rid, mtype, mamount, mdose, mbrand) " \
                    "values (%s, %s, %s, %s, %s) returning rid;"
            cursor.execute(query, (rid, mtype, amount, dose, brand,))
        # Medical devices
        elif category == "medical_devices":
            mtype = form['mdtype']
            brand = form['mdbrand']
            power_type = form['mdpower_type']
            precision = form['mdprecision']

            query = "insert into medical_devices(rid, mdtype, mdbrand, mdpower_type, mdprecision) " \
                    "values (%s, %s, %s, %s, %s) returning rid;"
            cursor.execute(query, (rid, mtype, brand, power_type, precision))
        # Clothes
        elif category == "clothes":
            brand = form['cbrand']
            gender = form['cgender']
            material = form['cmaterial']

            query = "insert into clothes(rid, cgender, cbrand, cmaterial) " \
                    "values (%s, %s, %s, %s) returning rid;"
            cursor.execute(query, (rid, gender, brand, material))
        # Power Generators
        elif category == "power_generators":
            brand = form['pgbrand']
            watts = form['pgwatts']
            gas = form['pggas']

            query = "insert into power_generators(rid, pgbrand, pgwatts, pggas) " \
                    "values (%s, %s, %s, %s) returning rid;"
            cursor.execute(query, (rid, brand, watts, gas,))
        # Batteries
        elif category == "batteries":
            btype = form['btype']
            size = form['bsize']
            brand = form['bbrand']

            query = "insert into batteries(rid, btype, bsize, bbrand) " \
                    "values (%s, %s, %s, %s) returning rid;"
            cursor.execute(query, (rid, btype, size, brand,))
        # Fuel
        elif category == "fuel":
            ftype = form['fltype']
            octane = form['floctane']
            brand = form['flbrand']

            query = "insert into fuel(rid, fltype, floctane, flbrand) " \
                    "values (%s, %s, %s, %s) returning rid;"
            cursor.execute(query, (rid, ftype, octane, brand,))
        # Tools
        elif category == "tools":
            ttype = form['ttype']
            brand = form['tbrand']

            query = "insert into tools(rid, ttype, tbrand) " \
                    "values (%s, %s, %s) returning rid;"
            cursor.execute(query, (rid, ttype, brand,))
        # Heavy Equipment
        elif category == "heavy_equipment":
            htype = form['hetype']
            brand = form['hebrand']
            size = form['hesize']
            weight = form['heweight']
            model = form['hemodel']

            query = "insert into heavy_equipment(rid, hetype, hebrand, hesize, heweight, hemodel) " \
                    "values (%s, %s, %s, %s, %s, %s) returning rid;"
            cursor.execute(query, (rid, htype, brand, size, weight, model,))
        else:
            return -1
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    # Gets the resources category
    def getResourceCategory(self, rid):
        cursor = self.conn.cursor()
        query = "select rcategory from resources where rid = %s"
        cursor.execute(query, (rid,))
        category = cursor.fetchone()[0]
        return category

    ##################################################
    #           Available resources methods          #
    ##################################################
    # Add resource to supplies table
    def insertSupplies(self, rid, sid, price):
        cursor = self.conn.cursor()
        query = "insert into supplies(rid, sid, sprice) values (%s, %s, %s) returning rid;"
        cursor.execute(query, (rid, sid, price,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    # Add resource to donations table
    def insertDonations(self, rid, sid):
        cursor = self.conn.cursor()
        query = "insert into donates(rid, sid) values (%s, %s) returning rid;"
        cursor.execute(query, (rid, sid,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    # Get the resources available for buying
    def getAllAvailable(self):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, sid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get available resources by id
    def getAvailableResourceById(self, rid):
        category = self.getResourceCategory(rid)
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, sid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select sid, firstname, lastname from supplier natural inner join appuser) " \
                "select * from resources natural inner join" \
                "((supplied natural inner join owner_info) natural inner join %s) " \
                "where rid = %s;"
        cursor.execute(query, (AsIs(category), rid,))
        result = cursor.fetchone()
        return result

    # Get available resources by name
    def getAvailableByName(self, name):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rname = %s"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get available by name, quantity and price
    def getAvailableByNameQuantityPrice(self, name, quantity, price):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rname = %s and rquantity>= %s and sprice<=%s;"
        cursor.execute(query, (name, quantity, price))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get available by name and price
    def getAvailableByNamePrice(self, name, price):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rname = %s and sprice<=%s;"
        cursor.execute(query, (name, price))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get available by name and quantity
    def getAvailableByNameQuantity(self, name, quantity):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in " \
                "(select rid from donates natural full join supplies) " \
                "and rname = %s and rquantity >= %s;"
        cursor.execute(query, (name, quantity))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get available based on price
    def getAvailableByPrice(self, price):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where sprice <= %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get available based on quantity
    def getAvailableByQuantity(self, quantity):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rquantity>=%s;"
        cursor.execute(query, (quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource list by category
    def getAvailableByCategory(self, category):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rcategory=%s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resource by name, price and quantity within a category
    def getAvailableInCategoryByNameQuantityPrice(self, category, name, quantity, price):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rcategory = %s and rname = %s and rquantity >= %s and sprice <= %s;"
        cursor.execute(query, (category, name, quantity, price,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource within a category by name and price
    def getAvailableInCategoryByNamePrice(self, category, name, price):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rcategory = %s and rname = %s and sprice <= %s;"
        cursor.execute(query, (category, name, price,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource within category by name and quantity
    def getAvailableInCategoryByNameQuantity(self, category, name, quantity):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rcategory = %s and rname = %s and rquantity >= %s;"
        cursor.execute(query, (category, name, quantity,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource within category by price and quantity
    def getAvailableInCategoryByPriceQuantity(self, category, price, quantity):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rcategory = %s and sprice <= %s and rquantity >= %s;"
        cursor.execute(query, (category, price, quantity,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource within category by price and quantity
    def getAvailableInCategoryByName(self, category, name):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rcategory = %s and rname = %s;"
        cursor.execute(query, (category, name,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource within category by price
    def getAvailableInCategoryByPrice(self, category, price):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rcategory = %s and sprice <= %s;"
        cursor.execute(query, (category, price,))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource within category by quantity
    def getAvailableInCategoryByQuantity(self, category, quantity):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rcategory = %s and rquantity >= %s;"
        cursor.execute(query, (category, quantity,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Inserts an available resource.
    def insertAvailable(self, name, quantity, category, price, form):
        # Insert general info
        rid = self.insert(name, quantity, category)
        # If insert unsuccessful then get out
        if rid == -1:
            print("FAILED FIRST INSERT")
            return rid
        # Supplier id
        sid = form['sid']
        # If price is 0 then resource is a donation
        if price == 0:
            rqid = self.insertDonations(rid, sid)
        else:
            rqid = self.insertSupplies(rid, sid, price)
        # If insert unsuccessful the get out
        if rqid == -1:
            print("FAILED SECOND INSERT")
            return rqid
        return self.insertSpecificResource(rid, category, form)

    ##################################################
    #           Requested resources methods          #
    ##################################################
    # Add resource to requests table
    def insertRequests(self, rid, nid):
        cursor = self.conn.cursor()
        query = "insert into requests(rid, nid) values (%s, %s) returning rid;"
        cursor.execute(query, (rid, nid,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    # Returns all the requests in the database
    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in (select rid from requests);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get a request by its id
    def getRequestedResourceById(self, rid):
        category = self.getResourceCategory(rid)
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join (requests natural inner join %s) where rid = %s;"
        cursor.execute(query, (AsIs(category), rid,))
        result = cursor.fetchone()
        return result

    # Get request by name
    def getRequestByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in(select rid from requests where rname = %s);"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get request by name and quantity
    def getRequestByNameQuantity(self, name, quantity):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join requests " \
                "where rname = %s and rquantity >= %s;"
        cursor.execute(query, (name, quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get request by quantity
    def getRequestByQuantity(self, quantity):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join requests " \
                "where rquantity >= %s;"
        cursor.execute(query, (quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource list by category
    def getRequestByCategory(self, category):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in (select rid from requests) " \
                "and rcategory=%s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resource within category by name and quantity
    def getRequestInCategoryByNameQuantity(self, category, name, quantity):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in (select rid from requests) " \
                "and rcategory = %s and rname = %s and rquantity >= %s;"
        cursor.execute(query, (category, name, quantity,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource within category by price and quantity
    def getRequestInCategoryByName(self, category, name):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in (select rid from requests) " \
                "and rcategory = %s and rname = %s;"
        cursor.execute(query, (category, name,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get resource within category by quantity
    def getRequestInCategoryByQuantity(self, category, quantity):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in (select rid from requests) " \
                "and rcategory = %s and rquantity >= %s;"
        cursor.execute(query, (category, quantity,))

        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Insert request for resource
    def insertRequest(self, name, quantity, category, form):
        # Insert general info
        rid = self.insert(name, quantity, category)
        # If insert unsuccessful then get out
        if rid == -1:
            return rid
        # Person in need id
        nid = form['nid']
        rqid = self.insertRequests(rid, nid)
        # If insert failed the get out
        if rqid == -1:
            return
        # Insert in specific resource
        return self.insertSpecificResource(rid, category, form)

    ##################################################
    #           Statistics methods                   #
    ##################################################

    # Get stats of the day
    def getDailyStats(self):
        result = []
        result_dict = {}
        # Gets current date
        now = datetime.datetime.now()
        # Saves current date in english format
        date_added = now.strftime("%d-%m-%Y")
        self.getDailyAvailable(result_dict, date_added)
        self.getDailyRequests(result_dict, date_added)
        self.getDailyCategoryCount(result_dict, date_added)
        result.append(result_dict)
        return result

    # Get stats of the week
    def getWeeklyStats(self):
        result = []
        result_dict = {}
        # Gets current date
        today = datetime.datetime.now()
        # What day of the week it is
        day = today.isoweekday()
        # Date difference between today and sunday
        diff = datetime.timedelta(days=day)
        # Date differecne between today and saturday
        day2 = 6 - day
        diff2 = datetime.timedelta(days=day2)
        # Start of week
        start = today - diff
        # End of week
        end = today + diff2
        # Change to string
        sunday = start.strftime("%d-%m-%Y")
        saturday = end.strftime("%d-%m-%Y")

        self.getWeeklyAvailable(result_dict, sunday, saturday)
        self.getWeeklyRequests(result_dict, sunday, saturday)
        self.getWeeklyCategoryCount(result_dict, sunday, saturday)
        result.append(result_dict)
        return result

    # Get stats of the regions
    # Eight senatorial districts:
    # San Juan, Bayamon, Arecibo, Mayaguez, Ponce, Guayama, Humacao, Carolina
    def getRegionalStats(self):
        pass

    # Gets daily available resources count
    # Returns the amount of available resources and how many were donated
    def getDailyAvailable(self, stat_dict, date_added):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select sum(rquantity) as available, sum(case when sprice = 0 then rquantity end) as donations, " \
                "sum(case when sprice != 0 then rquantity end) as supply " \
                "from resources natural inner join supplied " \
                "where rdate_added = %s"
        cursor.execute(query, (date_added,))
        data = cursor.fetchone()

        stat_dict['available'] = data[0]
        stat_dict['donations'] = data[1]
        stat_dict['onSale'] = data[2]
        return

    # Returns the amount of requested resources
    def getDailyRequests(self, stat_dict, date_added):
        cursor = self.conn.cursor()

        query = "select sum(rquantity) as requests " \
                "from resources natural inner join requests " \
                "where rdate_added = %s"
        cursor.execute(query, (date_added,))

        stat_dict['requests'] = cursor.fetchone()[0]

        return

    # Get quantity of resources of each category
    def getDailyCategoryCount(self, stat_dict, date_added):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select rcategory, " \
                "coalesce(sum(case when sprice is null then rquantity end),0) as request, " \
                "coalesce(sum(case when sprice >=0 then rquantity end), 0) as available " \
                "from resources natural inner join (supplied  natural full join requests) " \
                "where rdate_added = %s " \
                "group by rcategory " \
                "order by rcategory;"
        cursor.execute(query, (date_added,))

        for row in cursor:
            stat_dict[row[0]+' request'] = row[1]
            stat_dict[row[0]+' available'] = row[2]

        return

    # Gets Weekly available resources count
    # Returns the amount of available resources and how many were donated
    def getWeeklyAvailable(self, stat_dict, sunday, saturday):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select sum(rquantity) as available, sum(case when sprice = 0 then rquantity end) as donations, " \
                "sum(case when sprice != 0 then rquantity end) as supply " \
                "from resources natural inner join supplied " \
                "where rdate_added >= %s and rdate_added<= %s"
        cursor.execute(query, (sunday, saturday,))
        data = cursor.fetchone()

        stat_dict['available'] = data[0]
        stat_dict['donations'] = data[1]
        stat_dict['onSale'] = data[2]
        return

    # Returns the amount of requested resources
    def getWeeklyRequests(self, stat_dict, sunday, saturday):
        cursor = self.conn.cursor()

        query = "select sum(rquantity) as requests " \
                "from resources natural inner join requests " \
                "where rdate_added >= %s and rdate_added <= %s"
        cursor.execute(query, (sunday, saturday, ))

        stat_dict['requests'] = cursor.fetchone()[0]

        return

    # Get quantity of resources of each category
    def getWeeklyCategoryCount(self, stat_dict, sunday, saturday):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select rcategory, " \
                "coalesce(sum(case when sprice is null then rquantity end),0) as request, " \
                "coalesce(sum(case when sprice >=0 then rquantity end), 0) as available " \
                "from resources natural inner join (supplied  natural full join requests) " \
                "where rdate_added >= %s and rdate_added <= %s " \
                "group by rcategory " \
                "order by rcategory;"
        cursor.execute(query, (sunday, saturday, ))

        for row in cursor:
            stat_dict[row[0]+' request'] = row[1]
            stat_dict[row[0]+' available'] = row[2]

        return



