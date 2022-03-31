import pyodbc
import db_query as dbq

class Update:
    def __init__(self):
         self.db = pyodbc.connect(
                            'Driver={ODBC Driver 17 for SQL Server};'
                            'Server=sql.athena.domainhizmetleri.com;'
                            'Database=abdullah_pys;'
                            'UID=abdullah_pys;'
                            'PWD=@PassWord123;'
                            )
    def studentPasswordChange(self,student_no,old_pass,new_pass):
        query = dbq.Query()
        try:
            result = query.login_query(student_no,old_pass)
            if result == "ogrenci":
                cursor = self.db.cursor()
                cursor.execute("UPDATE m_Student SET password = ? WHERE studentID = ? AND password = ?", new_pass, student_no,old_pass)
                self.db.commit()
                return "Successful"
            else:
                return "False"
        except Exception as e:
            e = str(e)
            return e

nesne = Update()
print(nesne.studentPasswordChange("111","yeninew2","yeninew3"))
