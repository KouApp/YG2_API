import datetime

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
            try:
                curs = self.db.cursor()
                curs.execute('SELECT * FROM [abdullah_pys].[m_Faculty]')
                dataTable = curs.fetchall()
                for data in dataTable:
                    if data[0] == faculty_id:
                        dicte = {"1":data[0],
                                 "2":data[1]}
                        return dicte
                return "Bulunamadi"
            except Exception as e:
                e = str(e)
                return e
        else:
            return "False"

    def department_id_query(self,depart_id):
        if len(depart_id) == 4:
            try:
                curs = self.db.cursor()
                curs.execute('SELECT * FROM [abdullah_pys].[m_Department]')
                dataTable = curs.fetchall()
                for data in dataTable:
                    if data[0] == depart_id:
                        dicte = {"departmentID":data[0],
                                 "facultyID":data[1],
                                 "name":data[2]}
                        return dicte
                return "Bulunamadi"
            except Exception as e:
                e = str(e)
                return e
        else:
            return "False"

    def advisor_id_query(self,regist_id):
        try:
            if regist_id.isnumeric():
                curs = self.db.cursor()
                curs.execute('SELECT * FROM [abdullah_pys].[m_Advisor]')
                dataTable = curs.fetchall()
                for data in dataTable:
                    if data[0] == int(regist_id):
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
                return "Bulunamadi"
            else:
                return "Variable not int"

        except Exception as e:
            e = str(e)
            return e

    def message_id_query(self,msg_id):
        try:
            msg_id = str(msg_id)
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[t_message]')
            dataTable = curs.fetchall()
            if len(dataTable) == 0:
                return "NONE"
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
        except Exception as e:
            e = str(e)
            return e

    def student_id_query(self,student_id):
        try:
            if student_id.isnumeric():
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
                return "Bulunamadi"
            else:
                return "Variable not int"
        except Exception as e:
            e = str(e)
            return e

    def project_id_query(self,project_id):
        try:
            if project_id.isnumeric():
                curs = self.db.cursor()
                curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
                dataTable = curs.fetchall()
                for data in dataTable:
                    if data[1] == project_id:
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
                return "Bulunamadi"
            else:
                return "Variable not int"
        except Exception as e:
            e = str(e)
            return e

    def semester_id_query(self,semester_id):
        try:
            if semester_id.isnumeric():
                curs = self.db.cursor()
                curs.execute('SELECT * FROM [abdullah_pys].[m_semester]')
                dataTable = curs.fetchall()
                for data in dataTable:
                    if data[0] == int(semester_id):
                        dicte = {"id":data[0],
                                 "startDate":data[1],
                                 "endDate":data[2],
                                 "name":data[3]}
                        return dicte
                return "Bulunamadi"
            else:
                return "Variable not int"
        except Exception as e:
            e = str(e)
            return e

    def reports_id_query(self,reports_id):
        try:
            if reports_id.isnumeric():
                curs = self.db.cursor()
                curs.execute('SELECT * FROM [abdullah_pys].[t_reports]')
                dataTable = curs.fetchall()
                for data in dataTable:
                    if data[1] == int(reports_id):
                        dicte = {"id":data[0],
                                 "projectNumber":data[1],
                                 "pdfPath":data[2],
                                 "docPath":data[3],
                                 "status":data[4],
                                 "description":data[5],
                                 "insertionDate":data[6],
                                 "updateDate":data[7]}
                        return dicte
                return "Bulunamadi"
            else:
                return "Variable not int"
        except Exception as e:
            e = str(e)
            return e

    def dissertation_id_query(self,dis_id):
        try:
            if dis_id.isnumeric():
                curs = self.db.cursor()
                curs.execute('SELECT * FROM [abdullah_pys].[t_Dissertation]')
                dataTable = curs.fetchall()
                for data in dataTable:
                    if data[1] == int(dis_id):
                        dicte = {"id":data[0],
                                 "projectNumber":data[1],
                                 "pdfPath":data[2],
                                 "docPath":data[3],
                                 "status":data[4],
                                 "description":data[5],
                                 "insertionDate":data[6],
                                 "updateDate":data[7]}
                        return dicte
                return "Bulunamadi"
            else:
                return "Variable not int"
        except Exception as e:
            e = str(e)
            return e

    def status_id_query(self,status_id):
        try:
            if status_id.isnumeric():
                curs = self.db.cursor()
                curs.execute('SELECT * FROM [abdullah_pys].[m_Status]')
                dataTable = curs.fetchall()
                for data in dataTable:
                    if data[0] == int(status_id):
                        dicte = {"id":data[0],
                                 "name":data[1],
                                 "hexColorCode":data[2]}
                        return dicte
                return "Bulunamadi"
            else:
                return "Variable not int"
        except Exception as e:
            e = str(e)
            return e

    def superadmin_id_query(self,admin_id):
        try:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_superAdmin]')
            dataTable = curs.fetchall()
            for data in dataTable:
                if data[4] == admin_id:
                    dicte = {"id":data[0],
                             "name":data[1],
                             "surname":data[2],
                             "title":data[3],
                             "mail":data[4],
                             "password":data[5]}
                    return dicte
            return "Bulunamadi"
        except Exception as e:
            e = str(e)
            return e

    def login_query(self,no,password):
        try:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:
                if data[0].strip() == no and data[10]==password:
                    count += 1
                    return "student"

            curs1 = self.db.cursor()
            curs1.execute('SELECT * FROM [abdullah_pys].[m_superAdmin]')
            dataTable1 = curs1.fetchall()
            for data in dataTable1:
                if data[4] == no and data[5]==password:
                    count += 1
                    return "admin"

            curs2 = self.db.cursor()
            curs2.execute('SELECT * FROM [abdullah_pys].[m_Advisor]')
            dataTable2 = curs2.fetchall()
            for data in dataTable2:
                if data[0] == int(no) and data[8]==password:
                    count += 1
                    return "advisor"
            if count == 0:
                return "Bulunamadi"
        except Exception as e:
            e = str(e)
            return e

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
                    dicter = {"id":data[0],
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
                    dicte.update({count:dicter})
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def advisor_student_query(self,advisor_no):
        try:
            if advisor_no.isnumeric():
                curs = self.db.cursor()
                dicte = {}
                curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
                dataTable = curs.fetchall()
                count = 0
                for data in dataTable:
                    if data[1] == int(advisor_no):
                        count +=1
                        dicter = {"studentID":data[0],
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
                        dicte.update({count:dicter})
                return dicte
            else:
                return "Variable not int"
        except Exception as e:
            e = str(e)
            return e

    def proje_plagiarism_query(self,main_projeno):
        try:
            if main_projeno.isnumeric():
                curs = self.db.cursor()
                dicte = {}
                curs.execute('SELECT * FROM [abdullah_pys].[t_Plagiarism]')
                dataTable = curs.fetchall()
                count = 0
                for data in dataTable:

                    if data[1] == main_projeno:
                        count += 1
                        dicte.update({count : {int(data[2]):int(data[3])}})
                    if data[2] == main_projeno:
                        count += 1
                        dicte.update({count : {int(data[1]):int(data[3])}})
                return dicte
            else:
                return "Variable not int"
        except Exception as e:
            e = str(e)
            return e

    def semester_date_query(self):
        try:
            date = datetime.datetime.now()
            curs = self.db.cursor()
            dicte = {}
            curs.execute('SELECT * FROM [abdullah_pys].[m_semester]')
            dataTable = curs.fetchall()
            control =True
            for data in dataTable:
                if data[1] < date and data[2] > date:
                    control = False
                    dicte.update({"id" : data[0],
                                  "startdate":data[1],
                                  "enddate":data[2],
                                  "name":data[3]})
                    return dicte
            if control:
                data = dataTable[len(dataTable)-1]
                dicter = {"id" : data[0],
                          "startdate":data[1],
                          "enddate":data[2],
                          "name":data[3]}
                return dicter
        except Exception as e:
            e = str(e)
            return e

    def project_count_query(self,project_number):
        try:
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[t_reports]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:
                if int(data[1]) == int(project_number) and int(data[4]) == 4:
                    count +=1
            count_str = str(count)
            return str(count_str)
        except Exception as e:
            e = str(e)
            return e

    def advisor_query(self):
        try:
            dicte = {}
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Advisor]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:
                count += 1
                data = {"registrationID":data[0],
                        "name":data[1],
                        "surname":data[2],
                        "title":data[3],
                        "mail":data[4],
                        "departmentID":data[5],
                        "facultyID":data[6],
                        "photoPath":data[7],
                        "password":data[8]}
                dicte.update({count:data})
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def studentListQuery(self):
        try:
            dicte = {}
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_Student]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:
                count += 1
                data = {"studentID":data[0],
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
                dicte.update({count:data})
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def projectListQuery(self):
        try:
            dicte = {}
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:
                count += 1
                data = {"number":data[1],
                        "version":data[2],
                        "headline":data[3],
                        "matter":data[4],
                        "content":data[5],
                        "purpose":data[6],#
                        "keyword":data[7],
                        "materiel":data[8],
                        "method":data[9],
                        "possibility":data[10],
                        "status":data[11],
                        "description":data[12],
                        "maxPlagiarism":data[13],
                        "semesterID":data[14],
                        "studentID":data[15],
                        "insertionDate":data[16],
                        "updatedDate":data[17]}
                dicte.update({count:data})
            return dicte
        except Exception as e:
            e = str(e)
            return e

    def semesterListQuery(self):
        try:
            dicte = {}
            curs = self.db.cursor()
            curs.execute('SELECT * FROM [abdullah_pys].[m_semester]')
            dataTable = curs.fetchall()
            count = 0
            for data in dataTable:
                count += 1
                data = {"id":data[0],
                        "startDate":data[1],
                        "endDate":data[2],
                        "name":data[3]}
                dicte.update({count:data})
            return dicte
        except Exception as e:
            e = str(e)
            return e

# nse = Query()
# print(nse.semesterListQuery())
# print(nse.projectListQuery())
# print(nse.studentListQuery())
# print(nse.advisor_query())
# print(nse.project_count_query("1119881"))
# print(nse.semester_date_query())
# print(nse.message_id_query(2))
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
