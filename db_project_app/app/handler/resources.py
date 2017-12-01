
from flask import jsonify
from dao.resources import ResourcesDAO


class ResourcesHandler:
    # Builds dictionary with the row given
    def build_resource_dict(self, row):
        result = {}
        #result['rid'] = row[0]
        #result['rname'] = row[1]
        #result['rquantity'] = row[2]
        #result['rprice'] = row[3]
        result['rid'] = row['rid']
        result['rname'] = row['rname']
        result['rquantity'] = row['rquantity']
        result['rprice'] = row['rprice']
        result['sid'] = row['sid']
        return result

    ##################################################
    #           Available resources methods          #
    ##################################################
    # Get the resources available for buying
    def get_available_resources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllAvailable()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    # Get an available resource by its id
    def get_available_by_id(self, rid):
        dao = ResourcesDAO()
        row = dao.getAvailableResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such id."), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    # Get a list of the available resources with a given name
    def get_available_by_name(self, args):
        name = args.get("name")
        dao = ResourcesDAO()
        row = dao.getAvailableByName(name)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such name."), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

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
        else:
            return jsonify(Error="Bad request."), 400

    # Get available list by name quantity and price
    def get_available_by_name_quantity_price(self, name, quantity, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameQuantityPrice(name, quantity, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    # Get available list by name and price
    def get_available_by_name_price(self, name, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNamePrice(name, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    # Get available list by name and quantity
    def get_available_by_name_quantity(self, name, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByNameQuantity(name, quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    # Get list of products based on price
    def get_available_by_price(self, price):
        dao = ResourcesDAO()
        resource_list = dao.getAvailableByPrice(price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    ##################################################
    #           Requested resources methods          #
    ##################################################
    # Get list of all requests
    def get_requested_resources(self):
        dao = ResourcesDAO()
        resource_list = dao.getAllRequests()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    # Get a request by its id
    def get_request_by_id(self, rid):
        dao = ResourcesDAO()
        row = dao.getRequestResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such id."), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    # Get a list of the requests with a given name
    def get_request_by_name(self, name):
        dao = ResourcesDAO()
        row = dao.getRequestByName(name)
        if not row:
            return jsonify(Error="Resource Not Found. No resource with such name."), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

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
        else:
            return jsonify(Error="Bad request."), 400

    # Get request list by name quantity and price
    def get_request_by_name_quantity_price(self, name, quantity, price):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNameQuantityPrice(name, quantity, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    # Get request list by name and price
    def get_request_by_name_price(self, name, price):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNamePrice(name, price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    # Get request list by name and quantity
    def get_request_by_name_quantity(self, name, quantity):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByNameQuantity(name, quantity)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    # Get list of products based on price
    def get_request_by_price(self, price):
        dao = ResourcesDAO()
        resource_list = dao.getRequestByPrice(price)

        if not resource_list:
            return jsonify(Error="No such request found."), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)





