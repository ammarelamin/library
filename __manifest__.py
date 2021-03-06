{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Simple library management module',
    'category': 'education',
    'author': 'odoo techno-functional class',
    'maintainer': 'odoo techno-functional class',
    # 'website': '',
    # 'license': '',
    # 'contributors': [
    #     '',
    # ],
    'depends': [
        'sale_management',
    ],
    # 'external_dependencies': {
    #     'python': [
    #         '',
    #     ],
    # },
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/update_book_qty.xml',
        'views/sale.xml',
        'views/student.xml',
        'views/book.xml',
        'views/library.xml',
        'book_sequence.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
