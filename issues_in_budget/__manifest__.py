{
    'name': 'Adecuaciones Presupuestos',
    'version': '1.0',
    'summary': 'Campos personalizados',
    'description': 'Adecuaciones en el apartado de presupuestos solicitados por la empresa GTVP',
    'category': 'Personalizacion',
    'author': 'Xmarts',
    'website': 'www.xmarts.com',
    'depends': ['base',
                'account_budget',],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'aplication': True,
    'auto_install': False,

}


