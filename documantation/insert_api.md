# İnsert Post APİ
```
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'http://172.105.73.62:5000/studentInsert',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array('student_id' => '30','advisior_id' => '','name' => '','surname' => '','mail' => '','phone_no' => '','depart_id' => '','faculty_id' => '','clas' => '','photo_path' => '','password' => ''),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
###  studentInsert
http://172.105.73.62:5000/studentInsert   
request key = student_id,advisior_id,name,surname,mail,phone_no,depart_id,faculty_id,clas,photo_path,password  

###  facultyInsert
http://172.105.73.62:5000/facultyInsert   
request key = faculty_id,name  

###  departmentInsert
http://172.105.73.62:5000/departmentInsert   
request key = depart_id,faculty_id,name    

###  advisorInsert
http://172.105.73.62:5000/advisorInsert   
request key = reg_id,name,surname,title,mail,depart_id,faculty_id,photo_path,password   
  
###  messageInsert
http://172.105.73.62:5000/messageInsert   
request key = advisor_id,student_id,status,message    
  
###  dissertationInsert
http://172.105.73.62:5000/dissertationInsert   
id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate   

###  reportsInsert
http://172.105.73.62:5000/reportsInsert   
id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate   
  
###  plagiarismInsert
http://172.105.73.62:5000/plagiarismInsert   
id,mainprojeid,otherprojeid,plagrismrate   
  
###  semesterInsert
http://172.105.73.62:5000/semesterInsert   
id,startdate,enddate,name   

###  projectsInsert
http://172.105.73.62:5000/projectsInsert   
projects_insert  id,number,version,headline,matter,cont,purpose,keyword,metariel,method,poss,status,descr,maxplag,semeterid,studentid,insertiondate,updatedate   

