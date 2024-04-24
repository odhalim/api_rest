# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'web portal',
    'version': '16.0.1.0.0',
    'category': 'Accounting',
    'summary': 'api rest',
    'description': 'web portal',
    'sequence': '1',
    'author': 'Odoo',
    'license': 'LGPL-3',
    'depends': ['portal', 'website', 'hr'],
    'demo': [],
    'data': [
        'views/web_portal.xml',
        'views/website_dev.xml',
        'views/menu_website_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}
