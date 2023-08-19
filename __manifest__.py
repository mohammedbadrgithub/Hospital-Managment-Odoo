{
    'name':'Hospital Management System',
    'version':'1.0.0',
    'summary':'Hospital Management System can help in management all operation in hospital',
    'description':"""  This is 'Hospital Management System' that can manage hospital easy  """,
    'author':'Mohammed Badr',
    'website':"Mohammed.com",
    'application':True,
    'depends':['base'],
    'data':[
       
        'views/doctor_views.xml',
        'views/nurse_views.xml',
        'views/patient_views.xml',
        'views/specialize_views.xml',
        'views/ward_views.xml',
        # report
        'reports/doctor_report.xml',

        # security
        'security/security.xml',
        'security/ir.model.access.csv',
        
    ],
}