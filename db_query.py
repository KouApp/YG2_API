import pyodbc

class Query:
    def __init__(self):
         self.db = pyodbc.connect(
                            'Driver={ODBC Driver 17 for SQL Server};'
                            'Server=sql.athena.domainhizmetleri.com;'
                            'Database=abdullah_pys;'
                            'UID=abdullah_pys;'
                            'PWD=@PassWord123;'
                            )

    def faculty_id_query(self,faculty_id):
        #dicte = {"sorgu":""}
        if len(faculty_id) < 3:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Faculty]')
            dataTable = curs.fetchall()
            for data in dataTable:
                if data[0] == faculty_id:
                    #dicte["sorgu"] = data
                    return data
        else:
            return "False"

nse = Query()
print(nse.faculty_id_query("10"))
print(type(nse.faculty_id_query("10")))
