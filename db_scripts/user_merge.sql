INSERT INTO user_merged(csv_u_id,first_name, second_name, last_name, sex, birth_date, document_s, document_n)
SELECT DISTINCT id,FirstName,SecondName,LastName,Sex, Birthday, PassportS, PassportN
FROM csv_user;
