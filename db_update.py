import pyodbc
import db_query as dbq
import datetime

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

    def projectStatusUpdate(self,proje_no,new_status,old_status,desc,date):
        try:
            cursor = self.db.cursor()
            cursor.execute("UPDATE t_Projects SET status = ?,description = ?, updatedDate = ? WHERE number = ? AND status = ?", int(new_status), desc,date,proje_no,int(old_status))
            self.db.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def reportsStatusUpdate(self,proje_no,new_status,old_status,desc,date):
        try:

            cursor = self.db.cursor()
            cursor.execute("UPDATE t_reports SET status = ?,description = ?, updatedDate = ? WHERE projectNumber = ? AND status = ?", int(new_status), desc,date,proje_no,int(old_status))
            self.db.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def projectPlagiarismUpdate(self,proje_no):
        try:
            cursor = self.db.cursor()
            cursor.execute("UPDATE t_Projects SET status = ?,description = ? WHERE projectNumber = ? ", 5, "İntihal tespit edildi",proje_no)
            self.db.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

# nesne = Update()
# date = datetime.datetime.now()
# print(nesne.projectStatusUpdate("1124835",3,1,"yeni update",date))
# print(nesne.PasswordChange("pys@abdullahaligun.com","admin","yeninew4"))
