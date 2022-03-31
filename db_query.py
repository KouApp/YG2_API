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
        if len(faculty_id) < 3:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Faculty]')
            dataTable = curs.fetchall()
            for data in dataTable:
                if data[0] == faculty_id:
                    dicte = {"1":data[0],
                             "2":data[1]}
                    return dicte
        else:
            return "False"

    def department_id_query(self,depart_id):
        if len(depart_id) < 3:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Department]')
            dataTable = curs.fetchall()
            for data in dataTable:
                if data[0] == depart_id:
                    dicte = {"departmentID":data[0],
                             "facultyID":data[1],
                             "name":data[2]}
                    return dicte
        else:
            return "False"

    def advisor_id_query(self,regist_id):
        regist_id = int(regist_id)
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Advisor]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == regist_id:
                dicte = {"registrationID":data[0],
                         "name":data[1],
                         "surname":data[2],
                         "title":data[3],
                         "mail":data[4],
                         "departmentID":data[5],
                         "facultyID":data[6],
                         "photoPath":data[7],
                         "password":data[8]}
                return dicte
            else:
                return "False"

    def message_id_query(self,msg_id):
        msg_id = str(msg_id)
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_message]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == msg_id:
                dicte = {"id":data[0],
                         "advisorID":data[1],
                         "studentID":data[2],
                         "date":data[3],
                         "status":data[4],
                         "message":data[5]}
                return dicte
            else:
                return "False"

    def student_id_query(self,student_id):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0].split()[0] == student_id:
                dicte = {"studentID":data[0],
                         "advisorID":data[1],
                         "name":data[2],
                         "surname":data[3],
                         "mail":data[4],
                         "phoneNumber":data[5],
                         "departmentID":data[6],
                         "facultyID":data[7],
                         "class":data[8],
                         "photoPath":data[9],
                         "password":data[10]}
                return dicte
            else:
                return "False"

    def project_id_query(self,project_id):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == project_id:
                dicte = {"id":data[0],
                         "number":data[1],
                         "version":data[2],
                         "headline":data[3],
                         "matter":data[4],
                         "[content]":data[5],
                         "purpose":data[6],
                         "keyword":data[7],
                         "materiel":data[8],
                         "method":data[9],
                         "possibility":data[10],
                         "status":data[11],
                         "description":data[12],
                         "maxPlagiarism":data[13],
                         "semesterID":data[14],
                         "studentID":data[15],
                         "instertionDate":data[16],
                         "updateDate":data[17]}
                return dicte

    def semester_id_query(self,semester_id):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_semester]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == semester_id:
                dicte = {"id":data[0],
                         "startDate":data[1],
                         "endDate":data[2],
                         "name":data[3]}
                return dicte

    def plagiarism_id_query(self,pilagiarism_id):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Plagiarism]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == pilagiarism_id:
                dicte = {"id":data[0],
                         "mainProjeID":data[1],
                         "otherProjeID":data[2],
                         "plagiarismRate":data[3]}
                return dicte

    def reports_id_query(self,reports_id):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_reports]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == reports_id:
                dicte = {"id":data[0],
                         "projectNumber":data[1],
                         "pdfPath":data[2],
                         "docPath":data[3],
                         "status":data[4],
                         "description":data[5],
                         "insertionDate":data[6],
                         "updateDate":data[7]}
                return dicte

    def dissertation_id_query(self,dis_id):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Dissertation]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == dis_id:
                dicte = {"id":data[0],
                         "projectNumber":data[1],
                         "pdfPath":data[2],
                         "docPath":data[3],
                         "status":data[4],
                         "description":data[5],
                         "insertionDate":data[6],
                         "updateDate":data[7]}
                return dicte

    def status_id_query(self,status_id):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Status]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == status_id:
                dicte = {"id":data[0],
                         "name":data[1],
                         "hexColorCode":data[2]}
                return dicte

    def superadmin_id_query(self,admin_id):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_superAdmin]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] == admin_id:
                dicte = {"id":data[0],
                         "name":data[1],
                         "surname":data[2],
                         "title":data[3],
                         "mail":data[4],
                         "password":data[5]}
                return dicte

    def login_query(self,no,password):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0].strip() == no and data[10]==password:
                return "ogrenci"

        curs1 = self.db.cursor()
        curs1.execute('SELECT * FROM [abdullah_pys].[m_superAdmin]')
        dataTable1 = curs1.fetchall()
        for data in dataTable1:
            if data[4] == no and data[5]==password:
                return "superadmin"

        curs2 = self.db.cursor()
        curs2.execute('SELECT * FROM [abdullah_pys].[m_Advisor]')
        dataTable2 = curs2.fetchall()
        for data in dataTable2:
            if data[0] == int(no) and data[8]==password:
                return "advisor"

    def student_project_query(self,student_no):
        try:
            curs = self.db.cursor()
            dicte = {}
            curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:
                if data[15].strip() == student_no:
                    count +=1
                    dicte.update({count:data})
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def advisor_student_query(self,advisor_no):
        try:
            curs = self.db.cursor()
            dicte = {}
            curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:
                if data[1] == int(advisor_no):
                    count +=1
                    dicte.update({count:data})
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def proje_plagiarism_query(self,main_projeno):
        try:
            curs = self.db.cursor()
            dicte = {}
            curs.execute('SELECT * FROM [abdullah_pys].[t_Plagiarism]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:

                if int(data[1]) == main_projeno:
                    count += 1
                    dicte.update({count : {int(data[2]):int(data[3])}})
                if int(data[2]) == main_projeno:
                    count += 1
                    dicte.update({count : {int(data[1]):int(data[3])}})
            return dicte
        except Exception as e:
            e = str(e)
            return e
# nse = Query()
# print(nse.proje_plagiarism_query(1124835))
# print(nse.advisor_student_query(1))
# print(nse.student_project_query("111"))
# print(nse.student_advisor_query("111"))
# print(nse.login_query("1","paswrd")) # advisor
# print(nse.login_query("111","aad")) # student
# print(nse.login_query("pys@abdullahaligun.com","admin")) # super admin
# print(nse.reports_id_query(0))
# print(nse.plagiarism_id_query(0))
# print(nse.semester_id_query(0))
# print(nse.project_id_query(5))
# print(nse.message_id_query("1"))
# print(nse.advisor_id_query(2))
# print(nse.faculty_id_query("10"))
# print(nse.department_id_query("10"))
# print(type(nse.faculty_id_query("10")))
