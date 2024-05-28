# -*- coding: utf-8 -*-
###################################################################################

{
    'name': 'POS User Restrict',
    'summary': """Restricts User access to pos and orders""",
    'version': '16.0.1.0.0',
    'description': """Restricts User access to pos and orders""",
    'website': '',
    'category': 'Tools',
    'depends': ['point_of_sale','stock','purchase'],
    'license': 'AGPL-3',
    'data': [
        'security/security.xml',
        'views/res_users_inherit.xml'
    ],

    'installable': True,
    'auto_install': False,
}
