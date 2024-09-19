# -*- coding: utf-8 -*-
{
    'name': "WMS Integrator Module",

    'summary': """
        WMS Fields""",

    'description': """
        Modulo base para la integracion del WMS con Odoo
    """,

    'author': "Wonderbrands",
    'website': "https://wonderbrands.co/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
