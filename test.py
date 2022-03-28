import pyodbc

class test:
    def __init__(self):
        self.db = pyodbc.connect(
                            'Driver={ODBC Driver 17 for SQL Server};'
                            'Server=sql.athena.domainhizmetleri.com;'
                            'Database=abdullah_pys;'
                            'UID=abdullah_pys;'
                            'PWD=@PassWord123;'
                            )

    def student(self):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
        dataTable = curs.fetchall()
        for data in dataTable:
            try:
                assert type(data[0]) == int

            except AssertionError:
                print("{} string değil.".format(data[0]))


nesne = test()
nesne.student()

