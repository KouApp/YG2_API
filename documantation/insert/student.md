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
