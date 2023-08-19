import xmlrpc.client

url = 'http://localhost:8015'
db = 'hms_hospital'
username = 'admin'
password = 'admin'
# passwd = 'ae3aade8a63f42fed4f6ddf2a94caf31092d877b'


# connect = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common',format(url))
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# print(common.version())

# make authentication
uid = common.authenticate(db, username ,password , {} )

if uid :
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # models.execute_kw(db, uid, passwd, 'hms.specilize', 'check_access_rights', ['read'], {'raise_exception': False})
    
    
    # create new record 
    # models.execute_kw(db, uid, passwd, 'hms.specilize', 'create',[{'name':'ddddddd'}])
    
    
    
    # read only one record with condition
    records =  models.execute_kw(db, uid, passwd, 'hms.specilize', 'search',[[['name', '=', 'burning']]])
    
    
    # read all records
    records = models.execute_kw(db, uid, password, 'hms.specilize', 'search', [[]])
   
    
    # delete the record 
    # models.execute_kw(db, uid, password,  'hms.specilize', 'unlink', [[6]])
    print(records)
  

