import pyodbc


class Tester:
    def __init__(self):
        self.db = pyodbc.connect(
                            'Driver={ODBC Driver 17 for SQL Server};'
                            'Server=sql.athena.domainhizmetleri.com;'
                            'Database=abdullah_pys;'
                            'UID=abdullah_pys;'
                            'PWD=@PassWord123;'
                            )
    def faculty_list(self):
        print("----------------FACULTY DATA LİST-----------------------")
        print("----------------Faculty_id, Faculty_name----------------")
        print("--------------------------------------------------------")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Faculty]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print(data)

    def department_list(self):
        print("----------------DEPARTMENT DATA LİST-----------------------")
        print("----------------Department_id, Faculty_id, Department_name----------------")
        print("--------------------------------------------------------")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Department]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print(data)
    def student_list(self):
        print("----------------Student DATA LİST-----------------------")
        print("----------------Student_id, Faculty_id, Department_name----------------")
        print("--------------------------------------------------------")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print(data)
    def advisor_list(self):
        print("----------------Advisor DATA LİST-----------------------")
        print("----------------(registrationID,name,surname,title,mail,departmentID,facultyID,photoPath,password)----------------")
        print("--------------------------------------------------------")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Advisor]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print(data)
testing = Tester()
testing.faculty_list()
testing.department_list()
testing.student_list()
testing.advisor_list()
