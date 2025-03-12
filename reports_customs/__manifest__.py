# -*- coding: utf-8 -*-
# module template
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Invoice custom ',
    'version': '16.0',
    'author': "Udata",
    'depends': ['base','l10n_sa_edi' ],
    'data': [
          
           'views/report_invoice.xml',
           'views/base_document_layout.xml'

             ],
    'assets': {
        'web.report_assets_common': [
            'reports_customs/static/css/report_style.css',
        ],
        
    },
    'installable': True,
    'application': True,
}



