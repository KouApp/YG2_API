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
    def PasswordChange(self,no,old_pass,new_pass):
        query = dbq.Query()
        try:
            result = query.login_query(no,old_pass)
            if result == "ogrenci":
                cursor = self.db.cursor()
                cursor.execute("UPDATE m_Student SET password = ? WHERE studentID = ? AND password = ?", new_pass, no,old_pass)
                self.db.commit()
                return "Successful"
            elif result == "advisor":
                cursor = self.db.cursor()
                cursor.execute("UPDATE m_Advisor SET password = ? WHERE registrationID = ? AND password = ?", new_pass, int(no),old_pass)
                self.db.commit()
                return "Successful"
            elif result == "superadmin":
                cursor = self.db.cursor()
                cursor.execute("UPDATE m_superAdmin SET password = ? WHERE mail = ? AND password = ?", new_pass, no,old_pass)
                self.db.commit()
                return "Successful"
            else:
                return "False"
        except Exception as e:
            e = str(e)
            return e

# nesne = Update()
# print(nesne.PasswordChange("pys@abdullahaligun.com","admin","yeninew4"))
