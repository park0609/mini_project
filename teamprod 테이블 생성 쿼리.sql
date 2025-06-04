CREATE TABLE TEAMPROD (
	PROD_NUMBER NUMBER(6) PRIMARY KEY NOT NULL 
	,PROD_CATEGORY varchar(20) NOT NULL 
	,PROD_NAME varchar(20) NOT NULL 
	,PROD_PRICE NUMBER(6) NOT NULL
	,PROD_ADULT varchar(20) NOT NULL
	,PROD_AMOUNT NUMBER(6) 
);

SELECT * FROM teamprod;

INSERT ALL 
	INTO teamprod VALUES (1, 'snacks','cheetos',1500,'no',23)
	INTO teamprod VALUES (2, 'snacks','cornchip',1500,'no',17)
	INTO teamprod VALUES (3, 'snacks','pringles',4000,'no',20)
	INTO teamprod VALUES (4, 'snacks','vicpie',3200,'no',5)
	INTO teamprod VALUES (5, 'snacks','zec',1500,'no',31)
	INTO teamprod VALUES (6, 'snacks','bananakick',1700,'no',21)
	INTO teamprod VALUES (7, 'snacks','potatochip',1600,'no',7)
	INTO teamprod VALUES (8, 'snacks','doritos',1700,'no',13)
	INTO teamprod VALUES (9, 'snacks','pepero',1800,'no',34)
	INTO teamprod VALUES (10, 'snacks','binch',2400,'no',16)
	INTO teamprod VALUES (11, 'snacks','kicker',1000,'no',46)
	INTO teamprod VALUES (12, 'snacks','butterwaffle',3000,'no',18)
	INTO teamprod VALUES (13, 'snacks','postick',1700,'no',22)
	INTO teamprod VALUES (14, 'snacks','chocopie',4500,'no',10)
	INTO teamprod VALUES (15, 'beverage','caprisun',1700,'no',54)
	INTO teamprod VALUES (16, 'beverage','welchs',2000,'no',32)
	INTO teamprod VALUES (17, 'beverage','pepsi',2300,'no',27)
	INTO teamprod VALUES (18, 'beverage','milkiss',2200,'no',34)
	INTO teamprod VALUES (19, 'beverage','delmont',3400,'no',12)
	INTO teamprod VALUES (20, 'beverage','lipton',2000,'no',28)
	INTO teamprod VALUES (21, 'beverage','hotsix',1600,'no',30)
	INTO teamprod VALUES (22, 'beverage','pocarisweat',2800,'no',38)
	INTO teamprod VALUES (23, 'beverage','demisoda',1500,'no',22)
	INTO teamprod VALUES (24, 'beverage','narangd',1400,'no',33)
	INTO teamprod VALUES (25, 'ramen','shinramen',1200,'no',36)
	INTO teamprod VALUES (26, 'ramen','neoguri',1300,'no',23)
	INTO teamprod VALUES (27, 'ramen','jjapaghetti',1400,'no',42)
	INTO teamprod VALUES (28, 'ramen','jinramen',1200,'no',29)
	INTO teamprod VALUES (29, 'ramen','chamggaeramen',1400,'no',20)
	INTO teamprod VALUES (30, 'ramen','yeulramen',1600,'no',11)
	INTO teamprod VALUES (31, 'ramen','ggoggomen',1600,'no',5)
	INTO teamprod VALUES (32, 'drink','jinro',1800,'yes',40)
	INTO teamprod VALUES (33, 'drink','chamisul',1800,'yes',60)
	INTO teamprod VALUES (34, 'drink','saero',1800,'yes',43)
	INTO teamprod VALUES (35, 'drink','chueumchurum',1800,'yes',27)
	INTO teamprod VALUES (36, 'drink','hite',2600,'yes',16)
	INTO teamprod VALUES (37, 'drink','terra',1800,'yes',35)
	INTO teamprod VALUES (38, 'drink','cloud',1800,'yes',17)
	INTO teamprod VALUES (39, 'drink','crush',1800,'yes',16)
	INTO teamprod VALUES (40, 'sigarette','esse',4500,'yes',32)
	INTO teamprod VALUES (41, 'sigarette','theone',4500,'yes',25)
	INTO teamprod VALUES (42, 'sigarette','malboro',4500,'yes',38)
	INTO teamprod VALUES (43, 'sigarette','cammel',4500,'yes',11)
	INTO teamprod VALUES (44, 'sigarette','mevius',4500,'yes',42)
	INTO teamprod VALUES (45, 'sigarette','sevenstar',4500,'yes',4)
	INTO teamprod VALUES (46, 'necessaries','kleenex',2800,'no',3)
	INTO teamprod VALUES (47, 'necessaries','poppy',2600,'no',2)
	INTO teamprod VALUES (48, 'necessaries','oralb',2200,'no',6)
	INTO teamprod VALUES (49, 'necessaries','dentimate',2400,'no',8)
	INTO teamprod VALUES (50, 'necessaries','sensodyne',3000,'no',3)
	INTO teamprod VALUES (51, 'necessaries','perio',2800,'no',4)
	INTO teamprod VALUES (52, 'necessaries','elastine',3400,'no',2)
	INTO teamprod VALUES (53, 'necessaries','kerasys',3300,'no',3)
SELECT * FROM dual;

SELECT * FROM MINIPRO.DELIVERY4;

COMMIT;
SELECT * FROM teamprod;