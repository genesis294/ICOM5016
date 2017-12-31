from psycopg2._psycopg import AsIs

from config.dbconfig import pg_config
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

    # Deletes resource
    def delete(self, rid):
        cursor = self.conn.cursor()
        query = "delete from resources where rid = %s;"

        cursor.execute(query, (rid,))
        self.conn.commit()
        return rid

    # Update resource info. Can only update name and quantity.
    def update(self, rid, name, quantity):
        cursor = self.conn.cursor()
        query = "update resources set rname = %s, rquantity = %s where rid = %s;"
        cursor.execute(query, (name, quantity, rid,))
        self.conn.commit()
        return rid

    def updateQuantity(self, rid, quantity):
        cursor = self.conn.cursor()
        query = "update resources set rquantity = %s where rid = %s;"
        cursor.execute(query, (quantity, rid,))
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

    # Update specific resource
    def updateSpecificResource(self, rid, category, form):
        # We can now update in resource specific table
        # category will indicate in which table we can add the supply
        cursor = self.conn.cursor()
        # If resource is water
        if category == "water":
            wtype = form['wtype']
            brand = form['wbrand']

            query = "update water set wtype = %s, wbrand = %s where rid = %s;"
            cursor.execute(query, (wtype, brand, rid, ))
        # Ice
        elif category == "ice":
            size = form['isize']
            query = "update ice set isize = %s where rid = %s;"
            cursor.execute(query, (size, rid,))
        # Food
        elif category == "food":
            ftype = form['ftype']
            brand = form['fbrand']
            amount = form['famount']
            exp_date = form['fexp_date']
            query = "update food set ftype = %s, fbrand = %s, " \
                    "famount = %s, fexp_date = %s where rid = %s;"
            cursor.execute(query, (ftype, brand, amount, exp_date, rid))
        # Medication
        elif category == "medication":
            mtype = form['mtype']
            amount = form['mamount']
            dose = form['mdose']
            brand = form['mbrand']

            query = "update medication set mtype = %s, mamount = %s, " \
                    "mdose = %s, mbrand = %s where rid = %s;"
            cursor.execute(query, (mtype, amount, dose, brand, rid, ))
        # Medical devices
        elif category == "medical_devices":
            mtype = form['mdtype']
            brand = form['mdbrand']
            power_type = form['mdpower_type']
            precision = form['mdprecision']

            query = "update medical_devices set mdtype = %s, mdbrand = %s, " \
                    "mdpower_type = %s, mdprecision = %s where rid = %s;"
            cursor.execute(query, (mtype, brand, power_type, precision, rid, ))
        # Clothes
        elif category == "clothes":
            brand = form['cbrand']
            gender = form['cgender']
            material = form['cmaterial']

            query = "update clothes set cbrand = %s, " \
                    "cgender = %s, cmaterial = %s where rid = %s;"
            cursor.execute(query, (gender, brand, material, rid,))
        # Power Generators
        elif category == "power_generators":
            brand = form['pgbrand']
            watts = form['pgwatts']
            gas = form['pggas']

            query = "update power_generators set pgbrand = %s, " \
                    "pgwatts = %s, pggas = %s where rid = %s;"
            cursor.execute(query, (brand, watts, gas, rid, ))
        # Batteries
        elif category == "batteries":
            btype = form['btype']
            size = form['bsize']
            brand = form['bbrand']

            query = "update batteries set btype = %s, bsize = %s, " \
                    "bbrand = %s where rid = %s;"
            cursor.execute(query, (btype, size, brand, rid,))
        # Fuel
        elif category == "fuel":
            ftype = form['fltype']
            octane = form['floctane']
            brand = form['flbrand']

            query = "update fuel set fltype = %s, floctane = %s, " \
                    "flbrand = %s where rid = %s;"
            cursor.execute(query, (ftype, octane, brand, rid,))
        # Tools
        elif category == "tools":
            ttype = form['ttype']
            brand = form['tbrand']

            query = "update tools set ttype = %s, tbrand = %s " \
                    "where rid = %s;"
            cursor.execute(query, (ttype, brand, rid,))
        # Heavy Equipment
        elif category == "heavy_equipment":
            htype = form['hetype']
            brand = form['hebrand']
            size = form['hesize']
            weight = form['heweight']
            model = form['hemodel']

            query = "update heavy_equipment set hetype = %s, hebrand = %s, " \
                    "hesize = %s, heweight = %s, hemodel = %s " \
                    "where rid = %s;"
            cursor.execute(query, (htype, brand, size, weight, model, rid, ))
        else:
            return -1
        self.conn.commit()
        return rid

    # Gets the resources category
    def getResourceCategory(self, rid):
        cursor = self.conn.cursor()
        query = "select rcategory from resources where rid = %s"
        cursor.execute(query, (rid,))
        data = cursor.fetchone()
        if data:
            category = data[0]
        else:
            category = None
        return category

    # Deletes resource from a category
    def deleteFromCategory(self, rid, category):
        cursor = self.conn.cursor()
        query = "delete from %s where rid = %s;"

        cursor.execute(query, (AsIs(category), rid,))
        self.conn.commit()
        return rid

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

    # Update price of supply
    def updateSupplies(self, rid, price):
        cursor = self.conn.cursor()
        query = "update supplies set sprice = %s where rid = %s;"
        cursor.execute(query, (price, rid,))
        self.conn.commit()
        return rid

    # Get the resources available for buying
    def getAllAvailable(self):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
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
        if category:
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
        else:
            return None
    # Get resources based on name, quantity, price and location
    def getAvailableByNameQuantityPriceLocation(self, name, quantity, price, location):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select * " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "where rname = %s and rquantity>= %s and sprice<=%s and city = %s " \
                "order by rname"
        cursor.execute(query, (name, quantity, price, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resources based on name, price and location
    def getAvailableByNamePriceLocation(self, name, price, location):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select * " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "where rname = %s and sprice<=%s and city = %s " \
                "order by rname"
        cursor.execute(query, (name, price, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resources based on name, quantity and location
    def getAvailableByNameQuantityLocation(self, name, quantity, location):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select * " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "where rname = %s and rquantity>= %s and city = %s " \
                "order by rname"
        cursor.execute(query, (name, quantity, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAvailableByQuantityPriceLocation(self, quantity, price, location):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select * " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "where rquantity>= %s and sprice<=%s and city = %s " \
                "order by rname"
        cursor.execute(query, (quantity, price, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resources based on name and location
    def getAvailableByNameLocation(self, name, location):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select * " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "where rname = %s and city = %s " \
                "order by rname"
        cursor.execute(query, (name, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resources based on price and location
    def getAvailableByPriceLocation(self, price, location):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select * " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "where sprice<=%s and city = %s " \
                "order by rname"
        cursor.execute(query, (price, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resources based on quantity and location
    def getAvailableByQuantityLocation(self, quantity, location):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select * " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "where rquantity>= %s and city = %s " \
                "order by rname"
        cursor.execute(query, (quantity, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resources based on location
    def getAvailableByLocation(self, location):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select * " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "where city = %s " \
                "order by rname"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get available resources by name
    def getAvailableByName(self, name):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rname = %s"
                # "where rname ilike %s"
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

    # Get available by name and price
    def getAvailableByQuantityPrice(self, quantity, price):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rquantity >= %s and sprice<=%s;"
        cursor.execute(query, (quantity, price))
        result = []
        for row in cursor:
            result.append(row)
        return sorted(result, key=itemgetter(1))

    # Get available by name and quantity
    def getAvailableByNameQuantity(self, name, quantity):
        cursor = self.conn.cursor()
        query = "with supplied as (select rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select * from resources natural inner join supplied " \
                "where rname = %s and rquantity >= %s;"
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

    # Deletes resource from available list
    def deleteAvailable(self, rid):
        cursor = self.conn.cursor()
        query1 = "select exists( select * from donates where rid = %s)"
        cursor.execute(query1, (rid,))
        donates = cursor.fetchone()[0]
        if donates:
            query2 = "delete from donates where rid = %s;"
        else:
            query2 = "delete from supplies where rid = %s;"
        cursor.execute(query2, (rid,))
        self.conn.commit()
        self.deleteFromCategory(rid, self.getResourceCategory(rid))
        self.delete(rid)
        return rid

    # Update available resource
    def updateAvailable(self, rid, name, quantity, price, form):
        # Update general info
        rid = self.update(rid, name, quantity)
        # If price is 0 then resource is a donation
        if price != 0:
            self.updateSupplies(rid, price)
        return self.updateSpecificResource(rid, self.getResourceCategory(rid), form)

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
        query = "with owner_info as (select nid, firstname, lastname from person_in_need " \
                "natural inner join appuser) " \
                "select * from resources natural inner join" \
                "((requests natural inner join owner_info) natural inner join %s) " \
                "where rid = %s;"
        cursor.execute(query, (AsIs(category), rid,))
        result = cursor.fetchone()
        return result

    # Get request by name, quantity and location
    def getRequestByNameQuantityLocation(self, name, quantity, location):
        cursor = self.conn.cursor()
        query = "with owner_info as (select * " \
                "from person_in_need natural inner join (appuser natural inner join address) " \
                "select * from resources natural inner join (requests natural inner join owner_info)" \
                "where rname = %s and rquantity >= %s and city = %s" \
                "order by rname;"
        cursor.execute(query, (name, quantity, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resource by name and location
    def getRequestByNameLocation(self, name, location):
        cursor = self.conn.cursor()
        query = "with owner_info as (select * " \
                "from person_in_need natural inner join (appuser natural inner join address) " \
                "select * from resources natural inner join (requests natural inner join owner_info)" \
                "where rname = %s and city = %s" \
                "order by rname;"
        cursor.execute(query, (name, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resource by quantity and location
    def getRequestByQuantityLocation(self, quantity, location):
        cursor = self.conn.cursor()
        query = "with owner_info as (select * " \
                "from person_in_need natural inner join (appuser natural inner join address) " \
                "select * from resources natural inner join (requests natural inner join owner_info)" \
                "where rquantity = %s and city = %s" \
                "order by rname;"
        cursor.execute(query, (quantity, location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resource by location
    def getRequestByLocation(self, location):
        cursor = self.conn.cursor()
        query = "with owner_info as (select * " \
                "from person_in_need natural inner join (appuser natural inner join address) " \
                "select * from resources natural inner join (requests natural inner join owner_info)" \
                "where city = %s" \
                "order by rname;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get request by name
    def getRequestByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in(select rid from requests where rname = %s) " \
                "order by rname;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get request by name and quantity
    def getRequestByNameQuantity(self, name, quantity):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join requests " \
                "where rname = %s and rquantity >= %s " \
                "order by rname;"
        cursor.execute(query, (name, quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get request by quantity
    def getRequestByQuantity(self, quantity):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join requests " \
                "where rquantity >= %s " \
                "order by rname;"
        cursor.execute(query, (quantity,))
        result = []
        for row in cursor:
            result.append(row)
        return result

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
                "and rcategory = %s and rname = %s and rquantity >= %s" \
                "order by rname;"
        cursor.execute(query, (category, name, quantity,))

        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resource within category by price and quantity
    def getRequestInCategoryByName(self, category, name):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in (select rid from requests) " \
                "and rcategory = %s and rname = %s" \
                "order by rname;"
        cursor.execute(query, (category, name,))

        result = []
        for row in cursor:
            result.append(row)
        return result

    # Get resource within category by quantity
    def getRequestInCategoryByQuantity(self, category, quantity):
        cursor = self.conn.cursor()
        query = "select * from resources where rid in (select rid from requests) " \
                "and rcategory = %s and rquantity >= %s " \
                "order by rname;"
        cursor.execute(query, (category, quantity,))

        result = []
        for row in cursor:
            result.append(row)
        return result

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

    # Deletes requested resource
    def deleteRequest(self, rid):
        cursor = self.conn.cursor()
        query = "delete from requests where rid = %s;"
        cursor.execute(query, (rid,))
        self.conn.commit()
        self.deleteFromCategory(rid, self.getResourceCategory(rid))
        self.delete(rid)
        return rid

    # Update requested resource
    def updateRequest(self, rid, name, quantity, form):
        # Update general info
        rid = self.update(rid, name, quantity)
        return self.updateSpecificResource(rid, self.getResourceCategory(rid), form)

    ##################################################
    #           Statistics methods                   #
    ##################################################

    # Get stats of the day
    def getDailyStats(self):
        result_dict = {}
        # Gets current date
        now = datetime.datetime.now()
        # Saves current date in english format
        date_added = now.strftime("%d-%m-%Y")
        self.getDailyAvailable(result_dict, date_added)
        self.getDailyRequests(result_dict, date_added)
        self.getDailyCategoryCount(result_dict, date_added)
        return result_dict

    # Get stats of the week
    def getWeeklyStats(self):
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
        return result_dict

    # Get stats of the regions
    # Eight senatorial districts:
    # San Juan, Bayamon, Arecibo, Mayaguez, Ponce, Guayama, Humacao, Carolina
    def getRegionalStats(self):
        sanjuan = {'district': 'San Juan'}
        bayamon = {'district': 'Bayamon'}
        mayaguez = {'district': 'Mayaguez'}
        arecibo = {'district': 'Arecibo'}
        ponce = {'district': 'Ponce'}
        guayama = {'district': 'Guayama'}
        humacao = {'district': 'Humacao'}
        carolina = {'district': 'Carolina'}
        results = [arecibo, bayamon, carolina, guayama, humacao, mayaguez, ponce, sanjuan]
        self.getRegionalAvailable(results)
        self.getRegionalRequests(results)
        self.getRegionalCategoryCount(results)
        return results

    # Gets daily available resources count
    # Returns the amount of available resources and how many were donated
    def getDailyAvailable(self, stat_dict, date_added):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies) " \
                "select coalesce(sum(rquantity), 0) as available, " \
                "coalesce(sum(case when sprice = 0 then rquantity end), 0) as donations, " \
                "sum(case when sprice != 0 then rquantity end) as supply " \
                "from resources natural inner join supplied " \
                "where rdate_added = %s"
        cursor.execute(query, (date_added,))
        data = cursor.fetchone()

        if data[0]:
            stat_dict['available'] = data[0]
            stat_dict['donations'] = data[1]
            stat_dict['onSale'] = data[2]
        else:
            stat_dict['available'] = 0
            stat_dict['donations'] = 0
            stat_dict['onSale'] = 0
        return

    # Returns the amount of requested resources
    def getDailyRequests(self, stat_dict, date_added):
        cursor = self.conn.cursor()

        query = "select sum(rquantity) as requests " \
                "from resources natural inner join requests " \
                "where rdate_added = %s"
        cursor.execute(query, (date_added,))

        data = cursor.fetchone()[0]
        if data:
            stat_dict['requests'] = data
        else:
            stat_dict['requests'] = 0

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
            stat_dict[row[0] + '_request'] = row[1]
            stat_dict[row[0] + '_available'] = row[2]

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

        if data[0]:
            stat_dict['available'] = data[0]
            stat_dict['donations'] = data[1]
            stat_dict['onSale'] = data[2]
        else:
            stat_dict['available'] = 0
            stat_dict['donations'] = 0
            stat_dict['onSale'] = 0
        return

    # Returns the amount of requested resources
    def getWeeklyRequests(self, stat_dict, sunday, saturday):
        cursor = self.conn.cursor()

        query = "select sum(rquantity) as requests " \
                "from resources natural inner join requests " \
                "where rdate_added >= %s and rdate_added <= %s"
        cursor.execute(query, (sunday, saturday,))

        data = cursor.fetchone()[0]
        if data:
            stat_dict['requests'] = data
        else:
            stat_dict['requests'] = 0

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
        cursor.execute(query, (sunday, saturday,))

        for row in cursor:
            stat_dict[row[0] + '_request'] = row[1]
            stat_dict[row[0] + '_available'] = row[2]

        return

    # Gets Weekly available resources count
    # Returns the amount of available resources and how many were donated
    def getRegionalAvailable(self, stat_list):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select get_district(city) as district, coalesce(sum(rquantity), 0) as available, " \
                "coalesce(sum(case when sprice = 0 then rquantity end), 0) as donations, " \
                "coalesce(sum(case when sprice != 0 then rquantity end), 0) as supply " \
                "from resources natural inner join (supplied natural inner join owner_info) " \
                "group by district " \
                "order by district;"
        cursor.execute(query)
        i = 0
        for row in cursor:
            # If district isn't the same as the district from the list then values are 0
            while stat_list[i]['district'] != row[0]:
                stat_list[i]['available'] = 0
                stat_list[i]['donation'] = 0
                stat_list[i]['supply'] = 0
                i += 1

            stat_list[i]['available'] = row[1]
            stat_list[i]['donation'] = row[2]
            stat_list[i]['supply'] = row[3]
            i += 1
        while i < 8:
            stat_list[i]['available'] = 0
            stat_list[i]['donation'] = 0
            stat_list[i]['supply'] = 0
            i += 1
        return

    # Returns the amount of requested resources
    def getRegionalRequests(self, stat_list):
        cursor = self.conn.cursor()

        query = "with owner_info as (select uid, sid, city from supplier " \
                "natural inner join (appuser natural inner join address)) " \
                "select get_district(city) as district, sum(rquantity) as requests " \
                "from resources natural inner join (requests natural inner join owner_info) " \
                "group by district " \
                "order by district; "
        cursor.execute(query)

        # Index for stat list
        i = 0
        for row in cursor:
            # If the district in the row isn't the same as the list then the value is 0
            while stat_list[i]['district'] != row[0]:
                stat_list[i]['requests'] = 0
                i += 1

            stat_list[i]['requests'] = row[1]
            i += 1
        while i < 8:
            stat_list[i]['requests'] = 0
            i += 1
        return

    # Get quantity of resources of each category
    def getRegionalCategoryCount(self, stat_list):
        cursor = self.conn.cursor()

        query = "with supplied as (select sid, rid, coalesce(sprice, 0) as sprice " \
                "from donates natural full join supplies), " \
                "owner_info as (select uid, sid, city " \
                "from supplier natural inner join (appuser natural inner join address)) " \
                "select get_district(city) as district, rcategory, " \
                "coalesce(sum(case when sprice is null then rquantity end),0) as request, " \
                "coalesce(sum(case when sprice >=0 then rquantity end), 0) as available " \
                "from resources natural inner join ((supplied  natural full join requests) " \
                "natural inner join owner_info) " \
                "group by district, rcategory " \
                "order by district, rcategory; "
        cursor.execute(query)

        i = 0
        for row in cursor:
            if stat_list[i]['district'] == row[0]:
                stat_list[i][row[1] + '_request'] = row[2]
                stat_list[i][row[1] + '_available'] = row[3]
            else:
                while stat_list[i]['district'] != row[0]:
                    i += 1
                stat_list[i][row[1] + '_request'] = row[2]
                stat_list[i][row[1] + '_available'] = row[3]

        return




