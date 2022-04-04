from flask import Flask,jsonify,request
import db_insert
import db_query
import db_update
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
	semeterid = request.form['semeterid']
	studentid = request.form['studentid']
	insertiondate = request.form['insertiondate']
	updatedate = request.form['updatedate']
	insert = db_insert.Database_insert()
	result = insert.projects_insert(headline,matter,cont,
									purpose,keyword,metariel,
									method,poss,status,descr,
									semeterid,studentid,insertiondate,updatedate)
	return result

@app.route('/facultyQuery',methods=['POST'])
def facultyQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	que = db_query.Query()
	result = que.faculty_id_query(id)
	return result

@app.route('/departmentQuery',methods=['POST'])
def departmentQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	que = db_query.Query()
	result = que.department_id_query(id)
	return result

@app.route('/advisorQuery',methods=['POST'])
def advisorQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	que = db_query.Query()
	result = que.advisor_id_query(id)
	return result

@app.route('/messageQuery',methods=['POST'])
def messageQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	que = db_query.Query()
	result = que.message_id_query(id)
	return result

@app.route('/studentQuery',methods=['POST'])
def studentQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	que = db_query.Query()
	result = que.student_id_query(id)
	return result

@app.route('/projectQuery',methods=['POST'])
def projectQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	que = db_query.Query()
	result = que.project_id_query(id)
	return result

@app.route('/semesterQuery',methods=['POST'])
def semesterQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	que = db_query.Query()
	result = que.semester_id_query(id)
	return result

@app.route('/reportsQuery',methods=['POST'])
def reportsQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['projeno']
	que = db_query.Query()
	result = que.reports_id_query(id)
	return result

@app.route('/dissertationQuery',methods=['POST'])
def dissertationQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['projeno']
	que = db_query.Query()
	result = que.dissertation_id_query(id)
	return result

@app.route('/statusQuery',methods=['POST'])
def statusQuery():
	print('[INFO]--[test]--[FUNCTION]')
	id = request.form['id']
	que = db_query.Query()
	result = que.status_id_query(id)
	return result

@app.route('/superadminQuery',methods=['POST'])
def superadminQuery():
	print('[INFO]--[test]--[FUNCTION]')
	mail = request.form['mail']
	que = db_query.Query()
	result = que.superadmin_id_query(mail)
	return result

@app.route('/loginQuery',methods=['POST'])
def loginQuery():
	print('[INFO]--[test]--[FUNCTION]')
	no = request.form['no']
	password = request.form['password']
	que = db_query.Query()
	result = que.login_query(no,password)
	return result

@app.route('/studentProject',methods=['POST'])
def studentProject():
	print('[INFO]--[test]--[FUNCTION]')
	no = request.form['no']
	que = db_query.Query()
	result = que.student_project_query(no)
	return result

@app.route('/advisorStudent',methods=['POST'])
def advisorStudent():
	print('[INFO]--[test]--[FUNCTION]')
	no = request.form['no']
	que = db_query.Query()
	result = que.advisor_student_query(no)
	return result

@app.route('/plagiarismRate',methods=['POST'])
def plagiarismRate():
	print('[INFO]--[test]--[FUNCTION]')
	no = request.form['mainProjeid']
	que = db_query.Query()
	result = que.proje_plagiarism_query(no)
	return result

@app.route('/passwordChange',methods=['POST'])
def passwordChange():
	print('[INFO]--[test]--[FUNCTION]')
	no = request.form['no']
	old_password = request.form['old_pass']
	new_password = request.form['new_pass']
	update = db_update.Update()
	result = update.PasswordChange(no,old_password,new_password)
	return result

@app.route('/semesterDateQuery',methods=['POST'])
def semesterDateQuery():
	print('[INFO]--[test]--[FUNCTION]')
	que = db_query.Query()
	result = que.semester_date_query()
	return result

@app.route('/projectCounterQuery',methods=['POST'])
def projectCounterQuery():
	print('[INFO]--[test]--[FUNCTION]')
	projectNumber = request.form['proje_number']
	que = db_query.Query()
	result = que.project_count_query(projectNumber)
	return result

@app.route('/projectStatusUpdate',methods=['POST'])
def projectStatusUpdate():
	print('[INFO]--[test]--[FUNCTION]')
	projectNumber = request.form['proje_number']
	new_status = request.form['new_status']
	old_status = request.form['old_status']
	description = request.form['description']
	date = request.form['date']
	update = db_update.Update()
	result = update.projectStatusUpdate(projectNumber,new_status,old_status,description,date)
	return result

@app.route('/reportsStatusUpdate',methods=['POST'])
def reportsStatusUpdate():
	print('[INFO]--[test]--[FUNCTION]')
	projectNumber = request.form['proje_number']
	new_status = request.form['new_status']
	old_status = request.form['old_status']
	description = request.form['description']
	date = request.form['date']
	update = db_update.Update()
	result = update.reportsStatusUpdate(projectNumber,new_status,old_status,description,date)
	return result

@app.route('/dissertationStatusUpdate',methods=['POST'])
def dissertationStatusUpdate():
	print('[INFO]--[test]--[FUNCTION]')
	projectNumber = request.form['proje_number']
	new_status = request.form['new_status']
	old_status = request.form['old_status']
	description = request.form['description']
	update = db_update.Update()
	result = update.dissertationStatusUpdate(projectNumber,old_status,new_status,description)
	return result

@app.route('/advisorListQuery',methods=['POST'])
def advisorListQuery():
	print('[INFO]--[test]--[FUNCTION]')
	que = db_query.Query()
	result = que.advisor_query()
	return result

@app.route('/studentListQuery',methods=['POST'])
def studentListQuery():
	print('[INFO]--[test]--[FUNCTION]')
	que = db_query.Query()
	result = que.studentListQuery()
	return result

@app.route('/projectListQuery',methods=['POST'])
def projectListQuery():
	print('[INFO]--[test]--[FUNCTION]')
	que = db_query.Query()
	result = que.projectListQuery()
	return result

@app.route('/semesterListQuery',methods=['POST'])
def semesterListQuery():
	print('[INFO]--[test]--[FUNCTION]')
	que = db_query.Query()
	result = que.semesterListQuery()
	return result

@app.route('/advisorimport',methods=['POST'])
def advisorimport():
	print('[INFO]--[test]--[FUNCTION]')
	row = request.form['rowcount']
	base = request.form['base64']
	ins = db_insert.Database_insert()
	result = ins.adv_list_import(row,base)
	return result

@app.route('/studentimport',methods=['POST'])
def studentimport():
	print('[INFO]--[test]--[FUNCTION]')
	row = request.form['rowcount']
	base = request.form['base64']
	ins = db_insert.Database_insert()
	result = ins.student_list_import(row,base)
	return result



if __name__ == '__main__':
	app.run()
