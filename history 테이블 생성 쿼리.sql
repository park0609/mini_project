CREATE TABLE history(
       user_name varchar(30)
     , user_title varchar(30)
     , delivery_date varchar(30) NOT NULL
     , prod_category varchar(30)
     , prod_name varchar(30)
     , cell_amount number(20,0)
     , cell_price NUMBER(20,0) NOT NULL
);

COMMIT;

SELECT * FROM history;

ALTER TABLE HISTORY
MODIFY delivery_date varchar(30) NOT NULL;

ALTER TABLE history
MODIFY cell_price number(20, 0) NOT NULL;