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
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Faculty]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Faculty Data ### ",data)

    def department_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Department]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Department Data ### ",data)

    def student_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Student Data ### ",data)

    def advisor_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("ADVİSOR ### registrationID, name, surname, title, mail, departmentID, facultyID, photoPath,password")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Advisor]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Advisor Data ### ",data)

    def message_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("MESSAGE ### id,advisorİD,studentİD,date,status,message")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_message]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Message Data ### ",data)

    def status_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("STATUS ### id,name,hexcode")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Status]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Status Data ### ",data)

    def projects_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("PROJECTS ### id,name,hexcode")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Projects Data ### ",data)

    def semester_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("SEMESTER ### id,name,hexcode")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_semester]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Semester Data ### ",data)

    def dissertation_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Dissertation ### id,name,hexcode")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Dissertation]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("Dissertation Data ### ",data)

    def plagriasim_list(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("plagriasim ### id,name,hexcode")
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Plagiarism]')
        dataTable = curs.fetchall()
        for data in dataTable:
            print("plagriasim Data ### ",data)
testing = Tester()
# testing.faculty_list()
# testing.department_list()
testing.student_list()
testing.advisor_list()
testing.message_list()
testing.status_list()
testing.projects_list()
testing.semester_list()
testing.dissertation_list()
testing.plagriasim_list()
