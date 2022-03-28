# Query Post APİ
```
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'http://172.105.73.62:5000/facultyQuery',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => array('id' => '10'),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

###  facultyQuery
http://172.105.73.62:5000/facultyQuery   
request key = id  
request value = student no  

###  departmentQuery
http://172.105.73.62:5000/departmentQuery   
request key = id  
request value = depart no  

###  advisorQuery
http://172.105.73.62:5000/advisorQuery   
request key = id  
request value = advisor no  

###  messageQuery
http://172.105.73.62:5000/messageQuery   
request key = id  
request value = message no  

###  studentQuery
http://172.105.73.62:5000/studentQuery   
request key = id  
request value = student no  

###  projectQuery
http://172.105.73.62:5000/projectQuery   
request key = id  
request value = project no  

###  semesterQuery
http://172.105.73.62:5000/semesterQuery   
request key = id  
request value = semester no  

###  semesterQuery
http://172.105.73.62:5000/semesterQuery   
request key = id  
request value = semester no  

###  plagiarismQuery
http://172.105.73.62:5000/plagiarismQuery   
request key = id  
request value = plag no  

###  reportsQuery
http://172.105.73.62:5000/reportsQuery   
request key = id  
request value = reports no  

###  dissertationQuery
http://172.105.73.62:5000/dissertationQuery   
request key = id  
request value = dissert no  

###  statusQuery
http://172.105.73.62:5000/statusQuery   
request key = id  
request value = status no  

###  superadminQuery
http://172.105.73.62:5000/superadminQuery   
request key = id  
request value = superadmin no  
  
