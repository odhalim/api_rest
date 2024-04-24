# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class OdooRestApi(models.Model):
    _name = 'odoo.rest.api'
    _description = 'Odoo Rest Api'

    name = fields.Char(string='Name', required=True)
