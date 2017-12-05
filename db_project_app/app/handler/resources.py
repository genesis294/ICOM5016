
from flask import jsonify
from dao.resources import ResourcesDAO


class ResourcesHandler:
    # Builds dictionary with the row given
    # Req indicates if it's a request or if it is for available resources
    # Req = 1 is a request
    def build_resource_dict(self, row, req):
        result = {}
        #result['rid'] = row[0]
        #result['rname'] = row[1]
        #result['rquantity'] = row[2]
        #result['rprice'] = row[3]
        result['rid'] = row['rid']
        result['rname'] = row['rname']
        result['rquantity'] = row['rquantity']
        if req == 0:
            result['rprice'] = row['rprice']
        result['sid'] = row['sid']
        result['date_added'] = row['date_added']
        return result

    # Builds JSON to be sent
    def json_builder(self, list, req):
        result_list = []
        for row in list:
            result = self.build_resource_dict(row, req)
            result_list.append(result)
        return jsonify(Resources=result_list)

    ##################################################
    #           Available resources methods          #
    ##################################################
    # Get the resources available for buying
    def get_available_resources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllAvailable()
        return self.json_builder(resource_list, 0)

    # Get an available resource by its id
    def get_available_by_id(self, rid):
        dao = ResourcesDAO()
        row = dao.getAvailableResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such id."), 404
        else:
            resource = self.build_resource_dict(row, 0)
            return jsonify(Resource=resource)

    # Get a list of the available resources with a given name
    def get_available_by_name(self, name):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByName(name)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Searches for available resources that has the given parameters
    def search_for_available(self, args):
        name = args.get("name")
        quantity = args.get("quantity")
        price = args.get("price")

        if name and quantity and price:
            return self.get_available_by_name_quantity_price(name, quantity, price)
        elif name and price:
            return self.get_available_by_name_price(name, price)
        elif name and quantity:
            return self.get_available_by_name_quantity(name, quantity)
        elif name:
            return self.get_available_by_name(name)
        elif price:
            return self.get_available_by_price(price)
        elif quantity:
            return self.get_available_by_quantity(quantity)
        else:
            return jsonify(Error="Bad request."), 400

    # Get available list by name quantity and price
    def get_available_by_name_quantity_price(self, name, quantity, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameQuantityPrice(name, quantity, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get available list by name and price
    def get_available_by_name_price(self, name, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNamePrice(name, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get available list by name and quantity
    def get_available_by_name_quantity(self, name, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameQuantity(name, quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get list of products based on price
    def get_available_by_price(self, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByPrice(price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    # Get list of products based on price
    def get_available_by_quantity(self, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByQuantity(quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 0)

    def update_available(self, rid, resource):
        dao = ResourcesDAO();
        res = dao.getUpdateAvailable(rid, resource)
        return

    ##################################################
    #           Requested resources methods          #
    ##################################################
    # Get list of all requests
    def get_requested_resources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllRequests()
        return self.json_builder(resource_list, 1)

    # Get a request by its id
    def get_request_by_id(self, rid):
        dao = ResourcesDAO()
        row = dao.getRequestResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such id."), 404
        else:
            resource = self.build_resource_dict(row, 1)
            return jsonify(Resource=resource)

    # Get a list of the requests with a given name
    def get_request_by_name(self, name):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByName(name)
        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Searches for request that has the given parameters
    def search_for_request(self, args):
        name = args.get("name")
        quantity = args.get("quantity")
        price = args.get("price")

        if name and quantity and price:
            return self.get_request_by_name_quantity_price(name, quantity, price)
        elif name and price:
            return self.get_request_by_name_price(name, price)
        elif name and quantity:
            return self.get_request_by_name_quantity(name, quantity)
        elif name:
            return self.get_request_by_name(name)
        elif price:
            return self.get_request_by_price(price)
        elif quantity:
            return self.get_request_by_quantity(quantity)
        else:
            return jsonify(Error="Bad request."), 400

    # Get request list by name quantity and price
    def get_request_by_name_quantity_price(self, name, quantity, price):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNameQuantityPrice(name, quantity, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get request list by name and price
    def get_request_by_name_price(self, name, price):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNamePrice(name, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get request list by name and quantity
    def get_request_by_name_quantity(self, name, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNameQuantity(name, quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get list of products based on price
    def get_request_by_price(self, price):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByPrice(price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

    # Get list of products based on price
    def get_request_by_quantity(self, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByQuantity(quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            return self.json_builder(resource_list, 1)

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


