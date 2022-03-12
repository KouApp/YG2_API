import pyodbc


class TableControl:
    def __init__(self):
        self.db = pyodbc.connect(
                            'Driver={ODBC Driver 17 for SQL Server};'
                            'Server=sql.athena.domainhizmetleri.com;'
                            'Database=abdullah_pys;'
                            'UID=abdullah_pys;'
                            'PWD=@PassWord123;'
                            )
    def faculty_id_control(self,faculty_id):
        if len(faculty_id) < 2:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Faculty]')
            dataTable = curs.fetchall()
            for data in dataTable:
                if data[0] == faculty_id:
                    return True
            return False
        else:
            return False

    def department_id_control(self,department_id):
        if len(department_id) < 4:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Department]')
            dataTable = curs.fetchall()
            for data in dataTable:
                if data[0] == department_id:
                    return True
            return False
        else:
            return False

    def student_id_control(self,student_id):

        if len(student_id) < 9:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
            dataTable = curs.fetchall()
            for data in dataTable:
                if data[0].split()[0] == student_id:
                    return False
            return True
        else:
            return False

    def advisor_reg_control(self,reg_id):

        if type(reg_id) == int:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Advisor]')
            dataTable = curs.fetchall()
            for data in dataTable:
                if data[0] == reg_id:
                    return False
            return True
        else:
            return False
tableControl = TableControl()
# tableControl.faculty_id_control("2")
#print(tableControl.student_id_control("111"))
#print(tableControl.department_id_control("10"))
