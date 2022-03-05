import pyodbc
print(pyodbc.__file__)
db = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
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

