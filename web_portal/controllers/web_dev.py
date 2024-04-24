# -*- coding: utf-8 -*-
from odoo import http


class WebDev(http.Controller):

    @http.route('/hremployee/', auth='public', website=True)
    def index(self, **kw):
        # return http.request.render('web_portal.subjects', {'subjects': ['Python', 'Odoo', 'Django']})
        hr_employee = http.request.env['hr.employee'].sudo().search([])
        vals = {
            'employees': hr_employee
        }
        return http.request.render('web_portal.sale_orders', vals)

    @http.route('/hremployee/<model("hr.employee"):employee>/', auth='public', website=True)
    def display_name(self, employee):
        return http.request.render('web_portal.hr_employee_view', {'employee': employee})
