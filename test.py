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

    def projects_insert(self,number,version,headline,matter,cont,purpose,keyword,metariel,method,poss,status,descr,maxplag,semeterid,studentid,insertiondate,updatedate):
        try:
            curs = self.db.cursor()
            curs.execute("insert into t_Projects(number,version,headline,matter,[content],purpose,keyword,materiel,method,possibility,status,description,maxPlagiarism,semesterID,studentID,insertionDate,updatedDate) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            number,
                            version,
                            headline,
                             matter,
                             cont,
                             purpose,
                             keyword,
                             metariel,
                             method,
                             poss,
                             status,
                             descr,
                             maxplag,
                             semeterid,
                             studentid,
                             insertiondate,
                             updatedate)
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e




