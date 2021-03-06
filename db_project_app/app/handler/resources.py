
from flask import jsonify
from dao.resources import ResourcesDAO
from handler.users import UsersHandler


class ResourcesHandler:
    # Builds dictionary with the row given
    # Ava indicates if its an available resource
    # Ava = 1 means its an available resource
    def build_resource_dict(self, row, ava):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rquantity'] = row[2]
        result['rdate_added'] = row[3]
        result['rcategory'] = row[4]
        if ava:
            result['sprice'] = row[5]
        return result

    # Build dictionary based on the category of the resource
    # Ava indicates if its an available resource
    # Ava = 1 means its an available resource
    def build_resource_specific_dict(self, row, ava):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rquantity'] = row[2]
        result['rdate_added'] = row[3]
        result['rcategory'] = row[4]
        result['oid'] = row[5]
        category = row[4]
        n = 6
        if ava:
            result['sprice'] = row[6]
            n = n+1
        result['firstname'] = row[n]
        result['lastname'] = row[n+1]
        # If resource is water
        if category == "water":

            result['wid'] = row[n+2]
            result['wtype'] = row[n+3]
            result['wbrand'] = row[n+4]
        # Ice
        elif category == "ice":

            result['iid'] = row[n+2]
            result['isize'] = row[n+3]
        # Food
        elif category == "food":

            result['fid'] = row[n+2]
            result['ftype'] = row[n+3]
            result['fbrand'] = row[n+4]
            result['famount'] = row[n+5]
            result['fexp_date'] = row[n+6]
        # Medication
        elif category == "medication":

            result['mid'] = row[n+2]
            result['mtype'] = row[n+3]
            result['mamount'] = row[n+4]
            result['mdose'] = row[n+5]
            result['mbrand'] = row[n+6]
        # Medical devices
        elif category == "medical_devices":

            result['mdid'] = row[n+2]
            result['mdtype'] = row[n+3]
            result['mdbrand'] = row[n+4]
            result['mdpower_type'] = row[n+5]
            result['mdprecision'] = row[n+6]
        # Clothes
        elif category == "clothes":

            result['cid'] = row[n+2]
            result['cgender'] = row[n+3]
            result['cbrand'] = row[n+4]
            result['cmaterial'] = row[n+5]
        # Power Generators
        elif category == "power_generators":

            result['pgid'] = row[n+2]
            result['pgbrand'] = row[n+3]
            result['pgwatts'] = row[n+4]
            result['pggas'] = row[n+5]
        # Batteries
        elif category == "batteries":

            result['bid'] = row[n+2]
            result['btype'] = row[n+3]
            result['bsize'] = row[n+4]
            result['bbrand'] = row[n+5]
        # Fuel
        elif category == "fuel":

            result['flid'] = row[n+2]
            result['fltype'] = row[n+3]
            result['floctane'] = row[n+4]
            result['flbrand'] = row[n+5]
        # Tools
        elif category == "tools":

            result['tid'] = row[n+2]
            result['ttype'] = row[n+3]
            result['tbrand'] = row[n+4]
        # Heavy Equipment
        elif category == "heavy_equipment":

            result['heid'] = row[n+2]
            result['hetype'] = row[n+3]
            result['hebrand'] = row[n+4]
            result['hesize'] = row[n+5]
            result['heweight'] = row[n+6]
            result['hemodel'] = row[n+7]
        return result

    # Builds JSON to be sent
    # Ava indicates if its an available resource
    # Ava = 1 means its an available resource
    def json_builder(self, the_list, ava):
        result_list = []
        for row in the_list:
            result = self.build_resource_dict(row, ava)
            result_list.append(result)
        return jsonify(Resources=result_list)

    ##################################################
    #            General resource methods            #
    ##################################################
    # Get an resource by its id
    def get_resource_by_id(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such id."), 404
        else:
            resource = self.build_resource_dict(row, 0)
            return jsonify(Resource=resource)

    # Get all resources
    def get_all_resources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllResources()
        return self.json_builder(resource_list, 0)

    ##################################################
    #           Available resources methods          #
    ##################################################
    # Get the resources available for buying
    def get_available_resources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllAvailable()
        return self.json_builder(resource_list, 1)

    # Get available resource by id and category
    def get_available_by_id(self, rid):
        dao = ResourcesDAO()
        row = dao.getAvailableResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such id."), 404
        else:
            resource = self.build_resource_specific_dict(row, 1)
            return jsonify(Resource=resource)

    # Searches for available resources that has the given parameters
    def search_for_available(self, args):
        name = args.get("name")
        quantity = args.get("quantity")
        price = args.get("price")
        location = args.get("location")

        if name and quantity and price and location:
            return self.get_available_by_name_quantity_price_location(name, quantity, price, location)
        elif name and price and location:
            return self.get_available_by_name_price_location(name, price, location)
        elif name and quantity and location:
            return self.get_available_by_name_quantity_location(name, quantity, location)
        elif quantity and price and location:
            return self.get_available_by_quantity_price_location(quantity, price, location)
        elif name and location:
            return self.get_available_by_name_location(name, location)
        elif price and location:
            return self.get_available_by_price_location(price, location)
        elif quantity and location:
            return self.get_available_by_quantity_location(quantity, location)
        elif name and quantity and price:
            return self.get_available_by_name_quantity_price(name, quantity, price)
        elif name and price:
            return self.get_available_by_name_price(name, price)
        elif name and quantity:
            return self.get_available_by_name_quantity(name, quantity)
        elif quantity and price:
            return self.get_available_by_quantity_price(quantity, price)
        elif name:
            return self.get_available_by_name(name)
        elif location:
            return self.get_available_by_location(location)
        elif price:
            return self.get_available_by_price(price)
        elif quantity:
            return self.get_available_by_quantity(quantity)
        else:
            return jsonify(Error="Bad request."), 400

    # Get available list by name quantity, price and location
    def get_available_by_name_quantity_price_location(self, name, quantity, price, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameQuantityPriceLocation(name, quantity, price, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get available list by name, price and location
    def get_available_by_name_price_location(self, name, price, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNamePriceLocation(name, price, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get available list by name, quantity and location
    def get_available_by_name_quantity_location(self, name, quantity, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameQuantityLocation(name, quantity, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get available list by name, quantity and location
    def get_available_by_quantity_price_location(self, quantity, price, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByQuantityPriceLocation(quantity, price, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)
            # Get a list of the available resources with a given name

    def get_available_by_name_location(self, name, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameLocation(name, location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get list of products based on price and location
    def get_available_by_price_location(self, price, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByPriceLocation(price, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get list of products based on quantity and location
    def get_available_by_quantity_location(self, quantity, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByQuantityLocation(quantity, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get available list by name quantity and price
    def get_available_by_name_quantity_price(self, name, quantity, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameQuantityPrice(name, quantity, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get available list by name and price
    def get_available_by_name_price(self, name, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNamePrice(name, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get available list by name and quantity
    def get_available_by_name_quantity(self, name, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameQuantity(name, quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get available list by name and quantity
    def get_available_by_quantity_price(self, quantity, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByQuantityPrice(quantity, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get a list of the available resources with a given name
    def get_available_by_name(self, name):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByName(name)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get list of products based on price
    def get_available_by_price(self, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByPrice(price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get list of products based on quantity
    def get_available_by_quantity(self, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByQuantity(quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get all available resources of this category
    def get_available_by_category(self, category):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByCategory(category)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Search for resources within a category
    def search_for_available_in_category(self, category, args):
        name = args.get("name")
        quantity = args.get("quantity")
        price = args.get("price")
        location = args.get("location")

        if name and quantity and price and location:
            return self.get_available_in_category_by_name_quantity_price_location(category, name, quantity,
                                                                                  price, location)
        elif name and price and location:
            return self.get_available_in_category_by_name_price_location(category, name, price, location)
        elif name and quantity and location:
            return self.get_available_in_category_by_name_quantity_location(category, name, quantity, location)
        elif quantity and price and location:
            return self.get_available_in_category_by_quantity_price_location(category, quantity, price, location)
        elif name and location:
            return self.get_available_in_category_by_name_location(category, name, location)
        elif price and location:
            return self.get_available_in_category_by_price_location(category, price, location)
        elif quantity and location:
            return self.get_available_in_category_by_quantity_location(category, quantity, location)
        elif name and quantity and price:
            return self.get_available_in_category_by_name_quantity_price(category, name, quantity, price)
        elif name and price:
            return self.get_available_in_category_by_name_price(category, name, price)
        elif name and quantity:
            return self.get_available_in_category_by_name_quantity(category, name, quantity)
        elif price and quantity:
            return self.get_available_in_category_by_price_quantity(category, price, quantity)
        elif name:
            return self.get_available_in_category_by_name(category, name)
        elif price:
            return self.get_available_in_category_by_price(category, price)
        elif quantity:
            return self.get_available_in_category_by_quantity(category, quantity)
        elif location:
            return self.get_available_in_category_by_location(category, location)
        else:
            return jsonify(Error="Bad request."), 400

    def get_available_in_category_by_name_quantity_price_location(self, category, name, quantity,
                                                                  price, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByNameQuantityPriceLocation(category, name,
                                                                              quantity, price, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    def get_available_in_category_by_name_price_location(self, category, name, price, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByNamePriceLocation(category, name, price, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    def get_available_in_category_by_name_quantity_location(self, category, name, quantity, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByNameQuantityLocation(category, name, quantity, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    def get_available_in_category_by_quantity_price_location(self, category, quantity, price, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByQuantityPriceLocation(category, quantity, price, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    def get_available_in_category_by_name_location(self, category, name, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByNameLocation(category, name, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    def get_available_in_category_by_price_location(self, category, price, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByPriceLocation(category, price, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    def get_available_in_category_by_quantity_location(self, category, quantity, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByQuantityLocation(category, quantity, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    def get_available_in_category_by_location(self, category, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByLocation(category, location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get resource within category by name, quantity and price
    def get_available_in_category_by_name_quantity_price(self, category, name, quantity, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByNameQuantityPrice(category, name, quantity, price)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get resource within a category by name and price
    def get_available_in_category_by_name_price(self, category, name, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByNamePrice(category, name, price)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get name within a category by name and quantity
    def get_available_in_category_by_name_quantity(self, category, name, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByNameQuantity(category, name, quantity)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get name within a category by name and quantity
    def get_available_in_category_by_price_quantity(self, category, price, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByPriceQuantity(category, price, quantity)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get name within a category by name
    def get_available_in_category_by_name(self, category, name):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByName(category, name)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get name within a category by price
    def get_available_in_category_by_price(self, category, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByPrice(category, price)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get name within a category by quantity
    def get_available_in_category_by_quantity(self, category, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableInCategoryByQuantity(category, quantity)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get list of products based on location
    def get_available_by_location(self, location):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByLocation(location)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Insert available resource
    def insert_available_resource(self, form, price):
        # Get general resource info
        try:
            name = form['rname']
            quantity = form['rquantity']
            category = form['rcategory']
            category = category.rstrip().lower().replace(" ", "_")
            # If all this info was provided
            dao = ResourcesDAO()
            rid = dao.insertAvailable(name, quantity, category, price, form)
            # If -1 returned then the insert was not successful
            if rid == -1:
                print("FAILED THIRD INSERT")
                return jsonify(Error="Malformed post request"), 400
            result = dao.getAvailableResourceById(rid)
            return jsonify(Resource=result), 200
        except KeyError:
            print("DIDN'T EVEN TRY TO INSERT")
            return jsonify(Error="Malformed post request"), 400

    # Delete an available resource
    def delete_available_resource(self, rid):
        dao = ResourcesDAO()
        dao.deleteAvailable(rid)
        return jsonify(RID="Resource Deleted")

    # Update resource request
    def update_available_resource(self, rid, price, form):
        name = form['rname']
        quantity = form['rquantity']
        # If all this info was provided
        if name and quantity:
            dao = ResourcesDAO()
            # Update resource
            dao.updateAvailable(rid, name, quantity, price, form)
            result = dao.getRequestedResourceById(rid)
            return jsonify(Resource=result), 200
        return jsonify(Error="Malformed post request"), 400

    # Update resource quantity
    # This on is used when a purchase was made
    def update_available_quantity(self, rid, quantity):
        # Get general resource info
        if quantity >= 0:
            dao = ResourcesDAO()
            # Update resource
            dao.updateQuantity(rid, quantity)
            result = dao.getRequestedResourceById(rid)
            return jsonify(Resource=result), 200
        else:
            return jsonify(Error="Malformed post request"), 400

    # Gets all the users that have make a request for a given category
    def get_users_by_available_category(self, category):
        dao = ResourcesDAO()
        user_list = dao.getUsersByAvailableCategory(category)
        if not user_list:
            return jsonify(Error="No such request found."), 404
        else:
            result = []
            for row in user_list:
                user = UsersHandler().build_supplier_dict(row)
                result.append(user)
            return jsonify(Users=result), 200

    ##################################################
    #           Requested resources methods          #
    ##################################################
    # Get list of all requests
    def get_requested_resources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllRequests()
        return self.json_builder(resource_list, 0)

    # Get a request by its id
    def get_request_by_id(self, rid):
        dao = ResourcesDAO()
        row = dao.getRequestedResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such id."), 404
        else:
            resource = self.build_resource_specific_dict(row, 0)
            return jsonify(Resource=resource)

    # Get a list of the requests with a given name
    def get_request_by_name(self, name):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByName(name)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Searches for request that has the given parameters
    def search_for_request(self, args):
        name = args.get("name")
        quantity = args.get("quantity")
        location = args.get("location")

        if name and quantity and location:
            return self.get_request_by_name_quantity_location(name, quantity, location)
        elif name and location:
            return self.get_request_by_name_location(name, location)
        elif quantity and location:
            return self.get_request_by_quantity_location(quantity, location)
        elif name and quantity:
            return self.get_request_by_name_quantity(name, quantity)
        elif name:
            return self.get_request_by_name(name)
        elif location:
            return self.get_request_by_location(location)
        elif quantity:
            return self.get_request_by_quantity(quantity)
        else:
            return jsonify(Error="Bad request."), 400

    def get_request_by_name_quantity_location(self, name, quantity, location):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNameQuantityLocation(name, quantity, location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    def get_request_by_name_location(self, name, location):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNameLocation(name, location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    def get_request_by_quantity_location(self, quantity, location):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByQuantityLocation(quantity, location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    def get_request_by_location(self, location):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByLocation(location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get request list by name and quantity
    def get_request_by_name_quantity(self, name, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNameQuantity(name, quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get list of products based on quantity
    def get_request_by_quantity(self, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByQuantity(quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get all available resources of this category
    def get_request_by_category(self, category):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByCategory(category)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Search for resources within a category
    def search_for_request_in_category(self, category, args):
        name = args.get("name")
        quantity = args.get("quantity")
        location = args.get("location")

        if name and quantity and location:
            return self.get_request_in_category_by_name_quantity_location(category, name, quantity, location)
        elif name and location:
            return self.get_request_in_category_by_name_location(category, name, location)
        elif quantity and location:
            return self.get_request_in_category_by_quantity_location(category, quantity, location)
        elif name and quantity:
            return self.get_request_in_category_by_name_quantity(category, name, quantity)
        elif name:
            return self.get_request_in_category_by_name(category, name)
        elif quantity:
            return self.get_request_in_category_by_quantity(category, quantity)
        elif location:
            return self.get_request_in_category_by_location(category, location)
        else:
            return jsonify(Error="Bad request."), 400

    def get_request_in_category_by_name_quantity_location(self, category, name, quantity, location):
        dao = ResourcesDAO()
        resource_list = dao.getRequestInCategoryByNameQuantityLocation(category, name, quantity, location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    def get_request_in_category_by_name_location(self, category, name, location):
        dao = ResourcesDAO()
        resource_list = dao.getRequestInCategoryByNameLocation(category, name, location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    def get_request_in_category_by_quantity_location(self, category, quantity, location):
        dao = ResourcesDAO()
        resource_list = dao.getRequestInCategoryByQuantityLocation(category, quantity, location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    def get_request_in_category_by_location(self, category, location):
        dao = ResourcesDAO()
        resource_list = dao.getRequestInCategoryByLocation(category, location)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get resource within a category by quantity and name
    def get_request_in_category_by_name_quantity(self, category, name, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getRequestInCategoryByNameQuantity(category, name, quantity)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get resource within a category by name
    def get_request_in_category_by_name(self, category, name):
        dao = ResourcesDAO()
        resource_list = dao.getRequestInCategoryByName(category, name)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get name within a category by quantity
    def get_request_in_category_by_quantity(self, category, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getRequestInCategoryByQuantity(category, quantity)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Insert resource request
    def insert_requested_resource(self, form):
        # Get general resource info
        name = form['rname']
        quantity = form['rquantity']
        category = form['rcategory']
        category = category.rstrip().lower().replace(" ", "_")
        # If all this info was provided
        if name and quantity and category:
            dao = ResourcesDAO()
            # Insert request for resource
            rid = dao.insertRequest(name, quantity, category, form)
            # If -1 returned then the insert was not successful
            if rid == -1:
                return jsonify(Error="Malformed post request"), 400
            result = dao.getRequestedResourceById(rid)
            return jsonify(Resource=result), 200
        return jsonify(Error="Malformed post request"), 400

    # Delete a resource
    def delete_requested_resource(self, rid):
        dao = ResourcesDAO()
        dao.deleteRequest(rid)
        return jsonify(RID="Resource Deleted")

    # Update resource request
    def update_requested_resource(self, rid, form):
        # Get general resource info
        name = form['rname']
        quantity = form['rquantity']
        # If all this info was provided
        if name and quantity:
            dao = ResourcesDAO()
            # Update resource
            dao.updateRequest(rid, name, quantity, form)
            result = dao.getRequestedResourceById(rid)
            return jsonify(Resource=result), 200
        return jsonify(Error="Malformed post request"), 400

    # Gets all the users that have make a request for a given category
    def get_users_by_request_category(self, category):
        dao = ResourcesDAO()
        user_list = dao.getUsersByRequestCategory(category)
        if not user_list:
            return jsonify(Error="No such request found."), 404
        else:
            result = []
            for row in user_list:
                user = UsersHandler().build_person_in_need_dict(row)
                result.append(user)
            return jsonify(Users=result), 200

    ##################################################
    #           Statistic methods                    #
    ##################################################

    # Gets the daily statistics of the resources
    def get_daily_stats(self):
        dao = ResourcesDAO()
        return jsonify(stats=dao.getDailyStats())

    # Gets the weekly statistics of the resources
    def get_weekly_stats(self):
        dao = ResourcesDAO()
        return jsonify(stats=dao.getWeeklyStats())

    # Gets the weekly statistics of the resources
    def get_regional_stats(self):
        dao = ResourcesDAO()
        return jsonify(stats=dao.getRegionalStats())





