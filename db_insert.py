import pyodbc
import table_control as tableControl
import datetime
import full_text_search as fullSearch
import random

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
        status = int(status)
        if table_c.advisor_reg_control(advisor_id):
            return "Error code : 26"
        if table_c.student_id_control(student_id):
            return "Error code : 27"
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

    def plagiarism_insert(self,mainprojeid,otherprojeid,plagrismrate):
        try:
            curs = self.db.cursor()
            curs.execute("insert into t_Plagiarism(mainProjeID,otherProjeID,plagiarismRate) values (?,?,?)",
                         mainprojeid,
                         otherprojeid,
                         plagrismrate)
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e

    def semester_insert(self,id,startdate,enddate,name):
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

    def projects_insert(self,headline,matter,cont,purpose,keyword,
                        metariel,method,poss,status,descr,semeterid,
                        studentid,insertiondate,updatedate):
        try:
            version = 1
            deg = random.randint(1000,9999)
            number = str(studentid[:8]) + str(deg)
            curs = self.db.cursor()
            curs.execute("insert into t_Projects(number,version,headline,matter,[content],purpose,keyword,materiel,method,possibility,status,description,semesterID,studentID,insertionDate,updatedDate) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
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
                             semeterid,
                             studentid,
                             insertiondate,
                             updatedate)
            curs.commit()
            search = fullSearch.Search()
            search.allin(number)
            return "Successful"
        except Exception as e:
            e = str(e)
            return e


