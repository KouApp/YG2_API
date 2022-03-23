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
('/studentInsert',methods=['POST'])  
student_id,advisior_id,name,surname,mail,phone_no,depart_id,faculty_id,clas,photo_path,password   
  
('/facultyInsert',methods=['POST'])   
faculty_id,name  
  
('/departmentInsert',methods=['POST'])  
depart_id,faculty_id,name  
  
('/advisorInsert',methods=['POST'])  
reg_id,name,surname,title,mail,depart_id,faculty_id,photo_path,password  
  
('/messageInsert',methods=['POST'])  
advisor_id,student_id,status,message  
  
('/dissertationInsert',methods=['POST'])  
id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate  
  
('/reportsInsert',methods=['POST'])  
id,projenumber,pdfpath,docpath,status,desc,insertdate,updatedate  
  
('/plagiarismInsert',methods=['POST'])  
id,mainprojeid,otherprojeid,plagrismrate  
  
('/semesterInsert',methods=['POST'])  
id,startdate,enddate,name  
  
('/projectsInsert',methods=['POST'])  
projects_insert  id,number,version,headline,matter,cont,purpose,keyword,metariel,method,poss,status,descr,maxplag,semeterid,studentid,insertiondate,updatedate  
