CREATE TABLE CMEMBERLIST (
	user_name varchar(20) PRIMARY KEY NOT NULL 
	,user_title varchar(20) NOT NULL 
	,user_id varchar(20) NOT NULL 
	,user_pw NUMBER(6) CHECK (LENGTH(user_pw) = 6) NOT NULL
);

INSERT ALL 
INTO CMEMBERLIST VALUES ('박수민','manager','sumin0759@gmail.com',123456)
INTO CMEMBERLIST VALUES ('이동호','staff','dongho7736@gmail.com',123456)
INTO CMEMBERLIST VALUES ('박세찬','deliver','guppy135@naver.com',123456)
INTO CMEMBERLIST VALUES ('이경주','deliver','rudwnzlxl6@naver.com',123456)
SELECT * FROM dual; 

COMMIT ; 
SELECT * FROM CMEMBERLIST; 