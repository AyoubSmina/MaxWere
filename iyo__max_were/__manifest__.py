# -*- coding: utf-8 -*-
{
    'name': "iyo_MaxWere",
    'application':True,
    'sequence':'-1',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/view_persson.xml',
        'views/view_stagiaire.xml',
        'views/view_formateur.xml',
        'views/view_seance.xml',
        'views/view_module.xml',
        'views/view_inscription.xml',
        'views/Menu.xml',
               
    ],
}
