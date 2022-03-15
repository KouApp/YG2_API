import pyodbc
import table_control as tableControl
# print(pyodbc.__file__)
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
        curs = self.db.cursor()
        curs.execute("insert into m_Student(studentID,advisorID,name,surname,mail,phoneNumber,departmentID,facultyID,class,photoPath,password) values (?, ?,?,?,?,?,?,?,?,?,?)",
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
        return "Succesfull"

    def faculty_insert(self,faculty_id,name):
        table_c = tableControl.TableControl()
        if not table_c.faculty_id_control(faculty_id):
            if len(name) < 50:
                curs = self.db.cursor()
                curs.execute("insert into m_Faculty(facultyID, name) values (?, ?)", str(faculty_id), str(name))
                curs.commit()
                return "Succesfull"
            else:
                return "Error code : 13"
        else:
            return "Error code : 12"

    def department_insert(self,depart_id,faculty_id,name):
        table_c = tableControl.TableControl()
        if not table_c.department_id_control(depart_id):
            if not table_c.faculty_id_control(faculty_id):
                if len(name) < 55:
                    curs = self.db.cursor()
                    curs.execute("insert into m_Department(departmentID, facultyID, name) values (?, ?, ?)", str(depart_id), str(faculty_id),str(name))
                    curs.commit()
                    return "başarılı"
                else:
                    return "Error code : 15"
            else:
                return "Error code : 12"
        else:
            return "Error code : 14"

    def advisor_insert(self,reg_id,name,surname,title,mail,depart_id,faculty_id,photo_path,password):
        table_c = tableControl.TableControl()
        if not table_c.advisor_reg_control(reg_id):
            return "Error code : 16"
        if not len(name) < 105:
            return "Error code : 3"
        if not len(surname) < 50:
            return "Error code : 4"
        if not len(mail) < 255:
            return "Error code : 5"
        if not len(title) < 30:
            return "Error code : 17"
        if not table_c.department_id_control(depart_id):
            return "Error code : 7"
        if not table_c.faculty_id_control(faculty_id):
            return "Error code : 8"
        if not type(photo_path) == str:
            return "Error code : 10"
        if not len(password) < 255:
            return "Error code : 11"
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
        return "Succesfull"

    #id otomatik artıcak message
    def messsage_insert(self,id,advisor_id,student_id,status,message):
        table_c = tableControl.TableControl()
        date = datetime.datetime.now()
        if not len(id) < 10 and type(id) == str:
            return "Error code : 18"
        if table_c.advisor_reg_control(advisor_id):
            return "Error code : 19"
        if table_c.student_id_control(student_id):
            return "Error code : 20"
        if not type(status) == int:
            return "Error code : 20"
        if not type(message) == str:
            return "Error code : 21"
        curs = self.db.cursor()
        curs.execute("insert into t_message(id,advisorID,studentID,date,status,message) values (?,?,?,?,?,?)",
            str(id),
            int(advisor_id),
            str(student_id),
            date,
            int(status),
            str(message))
        curs.commit()
        return "Succesfull"

    def status_insert(self,id,name,hexcode):
        if not type(id) == str:
            return "Error code : 22"
        if not len(name) < 10 and type(name) == str:
            return "Error code : 23"
        if not type(hexcode) == str:
            return "Error code : 24"
        curs = self.db.cursor()
        curs.execute("insert into m_Status(id,name,hexColorCode) values (?,?,?)",
            id,
            name,
            hexcode)
        curs.commit()
        return "Succesfull"

    def dissertation_insert(self,id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate):
        if not type(id) == int:
            return "Error code : 25"
        if not type(projenumber) == str:
            return "Error code : 26"
        if not type(pdfpath) == str:
            return "Error code : 27"
        if not type(docpath) == str:
            return "Error code : 28"
        if not type(status) == int:
            return "Error code : 29"
        if not type(desc) == str:
            return "Error code : 30"

        curs = self.db.cursor()
        curs.execute("insert into m_Dissertation(id,projectNumber,pdfPath,docPath,status,description,insertionDate,updateDate) values (?,?,?,?,?,?,?,?)",
                        id,
                        projenumber,
                        pdfpath,
                        docpath,
                        status,
                        desc,
                        insertdate,
                        updatedate)
        curs.commit()
        return "Succesfull"

    def reports_insert(self,id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate):
        if not type(id) == int:
            return "Error code : 31"
        if not type(projenumber) == str:
            return "Error code : 32"
        if not type(pdfpath) == str:
            return "Error code : 33"
        if not type(docpath) == str:
            return "Error code : 34"
        if not type(status) == int:
            return "Error code : 35"
        if not type(desc) == str:
            return "Error code : 36"

        curs = self.db.cursor()
        curs.execute("insert into t_reports(id,projectNumber,pdfPath,docPath,status,description,insertionDate,updateDate) values (?,?,?,?,?,?,?,?)",
                        id,
                        projenumber,
                        pdfpath,
                        docpath,
                        status,
                        desc,
                        insertdate,
                        updatedate)
        curs.commit()
        return "Succesfull"

    def plagiarism_insert(self,id,mainprojeid,otherprojeid,plagrismrate):
        if not type(id) == int:
            return "Error code : 37"
        if not type(mainprojeid) == int:
            return "Error code : 38"
        if not type(otherprojeid) == int:
            return "Error code : 39"
        if not type(plagrismrate) == int:
            return "Error code : 40"
        curs = self.db.cursor()
        curs.execute("insert into t_Plagiarism(id,mainProjeID,otherProjeID,plagiarismRate) values (?,?,?,?)",
                        id,
                        mainprojeid,
                        otherprojeid,
                        plagrismrate)
        curs.commit()
        return "Succesfull"

    # date nereden gelecek ?
    def semester_insert(self,id,startdate,enddate,name):
        if not type(id) == int:
            return "Error code : 41"
        if not type(name) == str:
            return "Error code : 42"
        curs = self.db.cursor()
        curs.execute("insert into m_semester(id,startDate,endDate,name) values (?,?,?,?)",
                        id,
                        startdate,
                        enddate,
                        name)
        curs.commit()
        return "Succesfull"
    #Project tablosunda content ne ?

dbase = Database_insert()
#print(dbase.advisor_insert(3,"mert","taş","baslık","mail","10","1","5","paswrd"))
#a = dbase.student_insert("116",1,"aaaa","bbbb","awda","5123","10","1","12","addaw","aad")
#print(a)
#b = dbase.faculty_insert("2","bilisim")
#print(b)



