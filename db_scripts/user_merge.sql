INSERT INTO user_merged(csv_u_id,first_name, second_name, last_name, sex, birth_date, document_s, document_n) 
SELECT DISTINCT id,FirstName,SecondName,LastName,Sex, Birthday, PassportS, PassportN 
FROM csv_user; 

/*коррекция порядка имени и фамилии*/ 
select * from xlsx_user 
UPDATE xlsx_user 
SET PassengerLastName = xu.PassengerFirstName,PassengerFirstName = cu.FirstName 
FROM xlsx_user xu JOIN csv_user cu 
ON xu.PassengerLastName=cu.FirstName 
UPDATE xlsx_user 
SET PassengerLastName = xu.PassengerFirstName,PassengerFirstName = ju.first_name 
FROM xlsx_user xu JOIN json_user ju 
ON xu.PassengerFirstName=ju.last_name 
/*далее реальный мердж*/ 
SELECT * FROM user_merged 

UPDATE user_merged 
SET xlsx_u_id=xlu.id 
FROM user_merged um JOIN xlsx_user xlu 
ON xlu.PassengerFirstName=um.first_name AND xlu.PassengerLastName=um.last_name 


UPDATE user_merged 
SET json_u_id=ju.id 
FROM user_merged um JOIN json_user ju 
ON ju.first_name=um.first_name AND ju.last_name=um.last_name 

UPDATE user_merged 
SET xml_u_id=xmu.userid 
FROM user_merged um JOIN xml_user xmu 
ON xmu.firstname=um.first_name AND xmu.lastname=um.last_name

UPDATE user_merged 
SET tab_u_id=tu.[user_id],second_name=tu.LSName,document_n=tu.PassN, 
document_s=tu.PassS,birth_date=tu.PaxBirthDate 
FROM user_merged um JOIN tab_user tu 
ON (tu.PassS=um.document_s AND tu.PassN=um.document_n) 

INSERT INTO user_merged(tab_u_id,first_name,second_name,last_name,birth_date, 
document_s,document_n) 
SELECT DISTINCT user_id, LName, LSName, LSurname,PaxBirthDate, 
PassS,PassN 
FROM tab_user tu 
WHERE tu.user_id not in 
(SELECT tab_u_id FROM user_merged WHERE tab_u_id is not NULL);

UPDATE user_merged 
SET xlsx_u_id=xlu.id 
FROM user_merged um JOIN xlsx_user xlu 
ON xlu.PassengerFirstName=um.first_name AND xlu.PassengerLastName=um.last_name 

UPDATE user_merged 
SET json_u_id=ju.id 
FROM user_merged um JOIN json_user ju 
ON ju.first_name=um.first_name AND ju.last_name=um.last_name 

UPDATE user_merged 
SET xml_u_id=xmu.userid 
FROM user_merged um JOIN xml_user xmu 
ON xmu.firstname=um.first_name AND xmu.lastname=um.last_name


INSERT INTO user_merged(xlsx_u_id,first_name,second_name,last_name) 
SELECT DISTINCT id, PassengerFirstName, PassengerSecondName, PassengerLastName 
FROM xlsx_user 
WHERE xlsx_user.id not in 
(SELECT xlsx_u_id FROM user_merged WHERE xlsx_u_id is not NULL); 

UPDATE user_merged 
SET json_u_id=ju.id 
FROM user_merged um JOIN json_user ju 
ON ju.first_name=um.first_name AND ju.last_name=um.last_name 

UPDATE user_merged 
SET xml_u_id=xmu.userid 
FROM user_merged um JOIN xml_user xmu 
ON xmu.firstname=um.first_name AND xmu.lastname=um.last_name

INSERT INTO user_merged(json_u_id,first_name,last_name) 
SELECT DISTINCT id, first_name, last_name 
FROM json_user 
WHERE json_user.id not in 
(SELECT json_u_id FROM user_merged WHERE json_u_id is not NULL); 

UPDATE user_merged 
SET xml_u_id=xmu.userid 
FROM user_merged um JOIN xml_user xmu 
ON xmu.firstname=um.first_name AND xmu.lastname=um.last_name

INSERT INTO user_merged(json_u_id,first_name,last_name) 
SELECT DISTINCT userid, firstname, lastname 
FROM xml_user 
WHERE xml_user.userid not in 
(SELECT xml_u_id FROM user_merged WHERE xml_u_id is not NULL);