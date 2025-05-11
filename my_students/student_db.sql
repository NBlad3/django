CREATE TABLE student_account(
id int,
username varchar(255),
password varchar(255),
primary key (id)
);
 
CREATE TABLE student_info(
id int,
name varchar(255),
phone varchar(12),
email varchar(255),
address varchar(255),
primary key(id)
);
 
INSERT INTO student_account values(1,'tungdt','admin');
INSERT INTO student_account values(2,'hanntn','admin');
 
INSERT INTO student_info values(1,'Dao Thanh Tung','0382468008','tungdt@gmail.com','Hanoi');
 
INSERT INTO student_info values(2,'Nguyen Thanh Ngoc Han','0123908232','hanntn@gmail.com','HCMC');
 
SELECT * FROM student_account;
 
SELECT sa.password FROM student_account sa WHERE username = 'tung';