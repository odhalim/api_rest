# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager
from odoo import http
from odoo.http import request
from odoo.tools.translate import _


class PortalAccount(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        """ Prepare the values for rendering the portal home page."""
        values = super()._prepare_home_portal_values(counters)
        employee_count = request.env['hr.employee'].search_count([])
        values['hr_employee'] = employee_count
        return values

    @http.route(['/my/employee', '/my/employee/page/<int:page>'], type='http', auth="user", website=True)
    def portal_employee(self, page=1, sortby='name', search="", search_in='All',  **kwargs):
        """ Employee portal home page. this method is used to display the employee list in the portal"""
        employee_obj = request.env['hr.employee']
        # add sorted dictionary to sort the employee list
        searchbar_sortings = {'name': {'label': _('Name'), 'order': 'name'},
                              'job_id': {'label': _('Job'), 'order': 'job_id'},
                              'department_id': {'label': _('Department'), 'order': 'department_id'}}
        default_order_by = searchbar_sortings[sortby]['order']
        # add search_in bar to search the employee list
        search_list = {
            'All': {'label': 'All', 'input': 'All', 'domain': []},
            'Name': {'label': 'Name', 'input': 'Name', 'domain': [('name', 'ilike', search)]},
            'job_id': {'label': 'Job', 'input': 'job_id', 'domain': [('job_id', 'ilike', search)]},
            'department_id': {'label': 'Department', 'input': 'department_id',
                              'domain': [('department_id', 'ilike', search)]}
        }
        search_domain = search_list[search_in]['domain']
        # pager is to make how many records per page "Pagination"
        page_details = pager(
            url="/my/employee",
            total=employee_obj.search_count(search_domain),
            page=page,
            url_args={'sortby': sortby, 'search_in': search_in, 'search': search}, # url_args is to make the search and sortby bar work
            step=5
        )
        employee_ids = employee_obj.search(search_domain, limit=5, order=default_order_by,offset=page_details['offset'])
        request.session['my_projects_history'] = employee_ids.ids[:100]
        vals = {'employee_ids': employee_ids,
                'page_name': 'employee_lis_view',
                'pager': page_details,
                'sortby': sortby,
                'searchbar_sortings': searchbar_sortings,
                'search_in': search_in,
                'searchbar_inputs': search_list,
                'search': search}
        return request.render("web_portal.portal_employee", vals)

    @http.route(['/my/employee/<int:employee_id>'], type='http', auth="user", website=True)
    def portal_my_employee_form_view(self, employee_id, **kw):
        """ Employee portal home page. this method is used to display the employee form in the portal"""
        employee = request.env['hr.employee'].sudo().browse(employee_id)
        if not employee.exists():
            return request.redirect('/my/employees')  # Redirect to a list of employees or a 404 page
        vals = {"employee_id": employee, 'page_name': 'portal_my_employee_form_view'}
        # make the pagination for the employee form
        employee_record = request.env['hr.employee'].search([])
        employee_ids = employee_record.ids
        employee_index = employee_ids.index(employee_id)
        if employee_index != 0 and employee_ids[employee_index - 1]:
            vals['prev_record'] = '/my/employee/{}'.format(employee_ids[employee_index - 1])
        if employee_index < len(employee_ids) - 1 and employee_ids[employee_index + 1]:
            vals['next_record'] = '/my/employee/{}'.format(employee_ids[employee_index + 1])
        return request.render("web_portal.portal_my_employee_form_view", vals)

    @http.route(['/my/employee/print/<model("hr.employee"):employee_id>'], type='http', auth="user", website=True)
    def portal_my_employee_print(self, employee_id, **kw):
        """ This method is used to print the report in pdf format"""
        print("print employee", employee_id)
        return self._show_report(model=employee_id, report_type='pdf', report_ref='hr.report_employee_card', download=True)


    # add new form view to create employee
    @http.route(['/new/employee', '/my/employee/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_employee_create(self, **kw):
        """ This method is used to create the employee form in the portal"""
        vals = {'page_name': 'portal_my_employee_create'}
        return request.render("web_portal.portal_my_employee_create", vals)

    def new_method_to_make_pull_request(self):
        print("corriger le conflic)
