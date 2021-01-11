# -*- coding: utf-8 -*-
{
    'name': "Football",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['project',
            'base',
            'resource',
            'mail',
            'analytic',
            'hr_holidays',
            'hr_timesheet',
            'hr_attendance',
            'hr',
            'hr_contract',
            'web',
            'website',
            'web_tour',
                ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizards/create_footballer.xml',
        'data/data.xml',
        'reports/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
