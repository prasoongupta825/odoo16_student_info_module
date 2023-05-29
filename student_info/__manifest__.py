# -*- coding: utf-8 -*-
{
    'name': 'Student Info',
    'version': '1.0',
    'summary': 'Module for managing student information',
    'description': 'A module to store and manage student information',
    'author': 'Prasoon Gupta',
    'category': 'Education',
    'license': 'GPL-3',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/menu.xml',
        # 'data/student_sequence.xml',
        # 'reports/student_report_template.xml',
        # 'views/student_image.xml',
        # 'views/student_templates.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
