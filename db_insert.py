import pyodbc
import table_control as tableControl
import datetime

class Database_insert:

    def __init__(self):
        self.db = pyodbc.connect(
                            'Driver={ODBC Driver 17 for SQL Server};'
                            'Server=sql.athena.domainhizmetleri.com;'
                            'Database=abdullah_pys;'
                            'UID=abdullah_pys;'
                            'PWD=@PassWord123;'
                            )
    def test(self):
        imlec = self.db.cursor()
        imlec.execute('SELECT * FROM [abdullah_pys].[m_Student]')
        kullanicilar = imlec.fetchall()
        for i in kullanicilar:
            print(i)

    def student_insert(self,student_id,advisior_id,name,surname,mail,phone_no,depart_id,faculty_id,clas,photo_path,password):
        table_c = tableControl.TableControl()
        if not table_c.student_id_control(student_id):
            return "Error code : 1"
        if not type(advisior_id) == int:
            return "Error code : 2"
        if not len(name) < 105:
            return "Error code : 3"
        if not len(surname) < 55:
            return "Error code : 4"
        if not len(mail) < 255:
            return "Error code : 5"
        if not len(phone_no) < 255:
            return "Error code : 6"
        if not table_c.department_id_control(depart_id):
            return "Error code : 7"
        if not table_c.faculty_id_control(faculty_id):
            return "Error code : 8"
        if not len(clas) < 8:
            return "Error code : 9"
        if not type(photo_path) == str:
            return "Error code : 10"
        if not len(password) < 255:
            return "Error code : 11"
        try:
            curs = self.db.cursor()
            curs.execute(
                "insert into m_Student(studentID,advisorID,name,surname,mail,phoneNumber,departmentID,facultyID,class,photoPath,password) values (?, ?,?,?,?,?,?,?,?,?,?)",
                str(student_id),
                int(advisior_id),
                str(name),
                str(surname),
                str(mail),
                str(phone_no),
                str(depart_id),
                str(faculty_id),
                str(clas),
                str(photo_path),
                str(password))
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def faculty_insert(self,faculty_id,name):
        table_c = tableControl.TableControl()
        if not table_c.faculty_id_control(faculty_id):
            if len(name) < 50:
                try:
                    curs = self.db.cursor()
                    curs.execute("insert into m_Faculty(facultyID, name) values (?, ?)", str(faculty_id), str(name))
                    curs.commit()
                    return "Successful"
                except Exception as e:
                    e = str(e)
                    return e
            else:
                return "Error code : 13"
        else:
            return "Error code : 12"

    def department_insert(self,depart_id,faculty_id,name):
        table_c = tableControl.TableControl()
        if not table_c.department_id_control(depart_id):
            if not table_c.faculty_id_control(faculty_id):
                if len(name) < 55:
                    try:
                        curs = self.db.cursor()
                        curs.execute("insert into m_Department(departmentID, facultyID, name) values (?, ?, ?)",
                                     str(depart_id), str(faculty_id), str(name))
                        curs.commit()
                        return "Successful"
                    except Exception as e:
                        e = str(e)
                        return e
                else:
                    return "Error code : 16"
            else:
                return "Error code : 15"
        else:
            return "Error code : 14"

    def advisor_insert(self,reg_id,name,surname,title,mail,depart_id,faculty_id,photo_path,password):
        table_c = tableControl.TableControl()
        if not table_c.advisor_reg_control(reg_id):
            return "Error code : 17"
        if not len(name) < 105:
            return "Error code : 18"
        if not len(surname) < 50:
            return "Error code : 19"
        if not len(mail) < 255:
            return "Error code : 20"
        if not len(title) < 30:
            return "Error code : 21"
        if not table_c.department_id_control(depart_id):
            return "Error code : 22"
        if not table_c.faculty_id_control(faculty_id):
            return "Error code : 23"
        if not type(photo_path) == str:
            return "Error code : 24"
        if not len(password) < 255:
            return "Error code : 25"
        try:
            curs = self.db.cursor()
            curs.execute("insert into m_Advisor(registrationID,name,surname,title,mail,departmentID,facultyID,photoPath,password) values (?,?,?,?,?,?,?,?,?)",
                str(reg_id),
                str(name),
                str(surname),
                str(title),
                str(mail),
                str(depart_id),
                str(faculty_id),
                str(photo_path),
                str(password))
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def messsage_insert(self,advisor_id,student_id,status,message):
        table_c = tableControl.TableControl()
        date = datetime.datetime.now()
        if table_c.advisor_reg_control(advisor_id):
            return "Error code : 26"
        if table_c.student_id_control(student_id):
            return "Error code : 27"
        if not type(status) == int:
            return "Error code : 28"
        if not type(message) == str:
            return "Error code : 29"
        try:
            curs = self.db.cursor()
            curs.execute("insert into t_message(advisorID,studentID,date,status,message) values (?,?,?,?,?)",
                         int(advisor_id),
                         str(student_id),
                         date,
                         int(status),
                         str(message))
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def dissertation_insert(self,id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate):
        if not type(id) == int:
            return "Error code : 30"
        if not type(projenumber) == str:
            return "Error code : 31"
        if not type(pdfpath) == str:
            return "Error code : 32"
        if not type(docpath) == str:
            return "Error code : 33"
        if not type(status) == int:
            return "Error code : 34"
        if not type(desc) == str:
            return "Error code : 35"
        try:
            curs = self.db.cursor()
            curs.execute(
                "insert into t_Dissertation(id,projectNumber,pdfPath,docPath,status,description,insertionDate,updateDate) values (?,?,?,?,?,?,?,?)",
                id,
                projenumber,
                pdfpath,
                docpath,
                status,
                desc,
                insertdate,
                updatedate)
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def reports_insert(self,id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate):
        if not type(id) == int:
            return "Error code : 36"
        if not type(projenumber) == str:
            return "Error code : 37"
        if not type(pdfpath) == str:
            return "Error code : 38"
        if not type(docpath) == str:
            return "Error code : 39"
        if not type(status) == int:
            return "Error code : 40"
        if not type(desc) == str:
            return "Error code : 41"
        try:
            curs = self.db.cursor()
            curs.execute(
                "insert into t_reports(id,projectNumber,pdfPath,docPath,status,description,insertionDate,updateDate) values (?,?,?,?,?,?,?,?)",
                id,
                projenumber,
                pdfpath,
                docpath,
                status,
                desc,
                insertdate,
                updatedate)
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def plagiarism_insert(self,id,mainprojeid,otherprojeid,plagrismrate):
        if not type(id) == int:
            return "Error code : 42"
        if not type(mainprojeid) == int:
            return "Error code : 43"
        if not type(otherprojeid) == int:
            return "Error code : 44"
        if not type(plagrismrate) == int:
            return "Error code : 45"
        try:
            curs = self.db.cursor()
            curs.execute("insert into t_Plagiarism(id,mainProjeID,otherProjeID,plagiarismRate) values (?,?,?,?)",
                         id,
                         mainprojeid,
                         otherprojeid,
                         plagrismrate)
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def semester_insert(self,id,startdate,enddate,name):
        if not type(id) == int:
            return "Error code : 46"
        if not type(name) == str:
            return "Error code : 47"
        try:
            curs = self.db.cursor()
            curs.execute("insert into m_semester(id,startDate,endDate,name) values (?,?,?,?)",
                         id,
                         startdate,
                         enddate,
                         name)
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def projects_insert(self,id,number,version,headline,matter,cont,purpose,keyword,metariel,method,poss,status,descr,maxplag,semeterid,studentid,insertiondate,updatedate):
        id = int(id)
        if not type(id) == int:
            return "Error code : 48"
        if not type(number) == str:
            return "Error code : 49"
        version = int(version)
        if not type(version) == int:
            return "Error code : 50"
        if not type(headline) == str:
            return "Error code : 51"
        if not type(matter) == str:
            return "Error code : 52"
        if not type(cont) == str:
            return "Error code : 53"
        if not type(purpose) == str:
            return "Error code : 54"
        if not type(keyword) == str:
            return "Error code : 55"
        if not type(metariel) == str:
            return "Error code : 56"
        if not type(method) == str:
            return "Error code : 57"
        if not type(poss) == str:
            return "Error code : 58"
        status = int(status)
        if not type(status) == int:
            return "Error code : 59"
        if not type(descr) == str:
            return "Error code : 60"
        if not type(maxplag) == str:
            return "Error code : 61"
        semeterid = int(semeterid)
        if not type(semeterid) == int:
            return "Error code : 62"
        if not type(studentid) == str:
            return "Error code : 63"
        try:
            curs = self.db.cursor()
            curs.execute("insert into t_Projects(id,number,version,headline,matter,[content],purpose,keyword,materiel,method,possibility,status,description,maxPlagiarism,semesterID,studentID,insertionDate,updatedDate) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            id,
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
                             updatedate
                         )
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

# date = datetime.datetime.now()
# print(date)
#
# nesne = Database_insert()
# print(nesne.dissertation_insert(0,"0","test","test",0,"test",date,date))
# print(nesne.projects_insert(0,"0",0,"test headline",
#                             "test matter",
#                             "test content",
#                             "test purpose",
#                             "test keywords",
#                             "test metariel",
#                             "test method",
#                             "test poss",
#                             0,
#                             "test description",
#                             "0000000000",
#                             0,
#                             "112",
#                             "2022-03-30 14:29:39","2022-03-30 14:29:39"))
