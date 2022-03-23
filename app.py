from flask import Flask,jsonify,request
import db_insert
import db_query

# Fonksiyon isimlerini kontrol et
# nesneden çağırılan metodları kontrol et
# dönüş değerlerini kontrol et
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

@app.route('/test',methods=['POST'])
def test():
	print('[INFO]--[test]--[FUNCTION]')
	faculty_id = request.form['faculty_id']
	quer = db_query.Query()
	response = quer.faculty_id_query(faculty_id)
	return response

#student_id,advisior_id,name,surname,mail,phone_no,depart_id,faculty_id,clas,photo_path,password
@app.route('/studentInsert',methods=['POST'])
def studentInsert():
	print('[INFO]--[test]--[FUNCTION]')
	student_id = request.form['student_id']
	advisior_id = request.form['advisior_id']
	name = request.form['name']
	surname = request.form['surname']
	mail = request.form['mail']
	phone_no = request.form['phone_no']
	depart_id = request.form['depart_id']
	faculty_id = request.form['faculty_id']
	clas = request.form['clas']
	photo_path = request.form['photo_path']
	password = request.form['password']
	insert = db_insert.Database_insert()
	result = insert.student_insert(student_id,advisior_id,name,surname,mail,phone_no,depart_id,faculty_id,clas,photo_path,password)
	return result

# faculty_id,name
@app.route('/facultyInsert',methods=['POST'])
def facultyInsert():
	print('[INFO]--[test]--[FUNCTION]')
	faculty_id = request.form['faculty_id']
	name = request.form['name']
	insert = db_insert.Database_insert()
	result = insert.faculty_insert(faculty_id,name)
	return result

# depart_id,faculty_id,name
@app.route('/departmentInsert',methods=['POST'])
def departmentInsert():
	print('[INFO]--[test]--[FUNCTION]')
	faculty_id = request.form['faculty_id']
	depart_id = request.form['depart_id']
	name = request.form['name']
	insert = db_insert.Database_insert()
	result = insert.department_insert(depart_id,faculty_id,name)
	return result

# reg_id,name,surname,title,mail,depart_id,faculty_id,photo_path,password
@app.route('/advisorInsert',methods=['POST'])
def advisorInsert():
	print('[INFO]--[test]--[FUNCTION]')
	reg_id = request.form['reg_id']
	name = request.form['name']
	surname = request.form['surname']
	title = request.form['title']
	mail = request.form['mail']
	depart_id = request.form['depart_id']
	faculty_id = request.form['faculty_id']
	photo_path = request.form['photo_path']
	password = request.form['password']
	insert = db_insert.Database_insert()
	result = insert.advisor_insert(reg_id,name,surname,title,mail,depart_id,faculty_id,photo_path,password)
	return result

# advisor_id,student_id,status,message
@app.route('/messageInsert',methods=['POST'])
def messageInsert():
	print('[INFO]--[test]--[FUNCTION]')
	advisor_id = request.form['advisor_id']
	student_id = request.form['student_id']
	status = request.form['status']
	message = request.form['message']
	insert = db_insert.Database_insert()
	result = insert.messsage_insert(advisor_id,student_id,status,message)
	return result

# id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate
@app.route('/dissertationInsert',methods=['POST'])
def dissertationInsert():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	projenumber = request.form['projenumber']
	pdfpath = request.form['pdfpath']
	docpath = request.form['docpath']
	status = request.form['status']
	desc = request.form['desc']
	insertdate = request.form['insertdate']
	updatedate = request.form['updatedate']
	insert = db_insert.Database_insert()
	result = insert.dissertation_insert(id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate)
	return result

# id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate
@app.route('/reportsInsert',methods=['POST'])
def reportsInsert():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	projenumber = request.form['projenumber']
	pdfpath = request.form['pdfpath']
	docpath = request.form['docpath']
	status = request.form['status']
	desc = request.form['desc']
	insertdate = request.form['insertdate']
	updatedate = request.form['updatedate']
	insert = db_insert.Database_insert()
	result = insert.reports_insert(id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate)
	return result

# id,mainprojeid,otherprojeid,plagrismrate
@app.route('/plagiarismInsert',methods=['POST'])
def plagiarismInsert():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	mainprojeid = request.form['mainprojeid']
	otherprojeid = request.form['otherprojeid']
	plagrismrate = request.form['plagrismrate']
	insert = db_insert.Database_insert()
	result = insert.plagiarism_insert(id,mainprojeid,otherprojeid,plagrismrate)
	return result

# id,startdate,enddate,name
@app.route('/semesterInsert',methods=['POST'])
def semesterInsert():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	startdate = request.form['startdate']
	enddate = request.form['enddate']
	name = request.form['name']
	insert = db_insert.Database_insert()
	result = insert.semester_insert(id,startdate,enddate,name)
	return result

# projects_insert  id,number,version,headline,matter,cont,purpose,keyword,metariel,method,poss,status,descr,maxplag,semeterid,studentid,insertiondate,updatedate
@app.route('/projectsInsert',methods=['POST'])
def projectsInsert():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	number = request.form['number']
	version = request.form['version']
	headline = request.form['headline']
	matter = request.form['matter']
	cont = request.form['cont']
	purpose = request.form['purpose']
	keyword = request.form['keyword']
	metariel = request.form['metariel']
	method = request.form['method']
	poss = request.form['poss']
	status = request.form['status']
	descr = request.form['descr']
	maxplag = request.form['maxplag']
	semeterid = request.form['semeterid']
	studentid = request.form['studentid']
	insertiondate = request.form['insertiondate']
	updatedate = request.form['updatedate']
	insert = db_insert.Database_insert()
	result = insert.projects_insert(id,number,version,headline,matter,cont,purpose,keyword,metariel,method,poss,status,descr,maxplag,semeterid,studentid,insertiondate,updatedate)
	return result

if __name__ == '__main__':
	app.run()
