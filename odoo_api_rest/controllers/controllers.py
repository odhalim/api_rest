# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import logging
_logger = logging.getLogger(__name__)


class OdooApiRest(http.Controller):
    @http.route('/api/odoo_api_rest', auth='public')
    def index(self, **kw):
        print("inside the api rest")
        sale_order = http.request.env['sale.order'].sudo().search([])
        output = "<h1>sale order</h1>"
        for order in sale_order:
            output += "<p>%s</p>" % order.name
        return output

    @http.route('/api/odoo_api_rest/get_data', website=True, csrf=False, type='http', methods=['GET', 'POST'])
    def hello(self, **kw):
        print("inside the api rest")
        output = "<h1>sale order</h1>"
        return output

    # @http.route('/api/odoo_api_rest', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"
    #
    # @http.route('/api/odoo_api_rest/get_data', auth='public', type='json')
    # def get_data(self, **kw):
    #     data = request.env['res.partner'].sudo().search_read([], ['name', 'email', 'phone'])
    #     return data
    #
    # @http.route('/api/odoo_api_rest/create_data', auth='public', type='json')
    # def create_data(self, **kw):
    #     data = request.env['res.partner'].sudo().create({
    #         'name': 'Test',
    #         'email': 'for test',
    #         'phone': '123456789'
    #     })
    #     return data

