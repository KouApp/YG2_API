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
            if result == "student":
                cursor = self.db.cursor()
                cursor.execute("UPDATE m_Student SET password = ? WHERE studentID = ? AND password = ?", no, no,old_pass)
                self.db.commit()
                return "Successful"
            elif result == "advisor":
                cursor = self.db.cursor()
                cursor.execute("UPDATE m_Advisor SET password = ? WHERE registrationID = ? AND password = ?", no, int(no),old_pass)
                self.db.commit()
                return "Successful"
            elif result == "admin":
                cursor = self.db.cursor()
                cursor.execute("UPDATE m_superAdmin SET password = ? WHERE mail = ? AND password = ?", no, no,old_pass)
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

    def reportsStatusUpdate(self,id,new_status,desc):
        try:
            date = datetime.datetime.now()
            cursor = self.db.cursor()
            cursor.execute("UPDATE t_reports SET status = ?,description = ?, updatedDate = ? WHERE projectNumber = ?",
                           int(new_status), desc,date,id)
            self.db.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def projectPlagiarismUpdate(self,proje_no):
        try:
            cursor = self.db.cursor()
            cursor.execute("UPDATE t_Projects SET status = ?,description = ? WHERE number = ? ", 5, "İntihal tespit edildi",proje_no)
            self.db.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def projectNewPlagiarismUpdate(self,proje_no,plag):
        try:
            cursor = self.db.cursor()
            cursor.execute("UPDATE t_Projects SET maxPlagiarism = ? WHERE number = ? ", plag,proje_no)
            self.db.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def dissertationStatusUpdate(self,id,new_status,desc):
        try:
            date = datetime.datetime.now()
            cursor = self.db.cursor()
            cursor.execute("UPDATE t_Dissertation SET status = ?,description=?,updatedDate=? WHERE id = ?",
                           new_status,desc,date,id)
            self.db.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

# nesne = Update()
# print(nesne.dissertationStatusUpdate("1119881",0,2,"yeni acıklama"))
# print(nesne.projectNewPlagiarismUpdate("1119416",14))
# date = datetime.datetime.now()
# print(nesne.projectStatusUpdate("1124835",3,1,"yeni update",date))
# print(nesne.PasswordChange("pys@abdullahaligun.com","admin","yeninew4"))
