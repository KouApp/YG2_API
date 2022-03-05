import pyodbc
print(pyodbc.__file__)
db = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=sql.athena.domainhizmetleri.com;'
    'Database=abdullah_pys;'
    'UID=abdullah_pys;'
    'PWD=@PassWord123;'
)
imlec = db.cursor()
imlec.execute('SELECT * FROM [abdullah_pys].[test_table]')
kullanicilar = imlec.fetchall()
for i in kullanicilar:
    print(i)
"""
    DBMS: Microsoft
    SQL
    Server(ver.
    15.00
    .2080)
    Case
    sensitivity: plain = mixed, delimited = mixed
    Driver: Microsoft
    JDBC
    Driver
    9.4
    for SQL Server(ver. 9.4.0.0, JDBC4.2)
    Ping: 33
    ms
    
"""