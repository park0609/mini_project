CREATE TABLE BRAND( 
		prod_number number(20,0) PRIMARY KEY NOT NULL --상품번호(프라이머리 키 )
		, prod_category varchar(30) NOT NULL -- 상품 분류 카테고리  
		, prod_name varchar2(20) NOT NULL -- 상품 이름 
		, prod_brand varchar(20) NOT NULL -- 브랜드 명  
);

INSERT ALL 
	-- 상품 상위 카테고리 snacks/ beverage / ramen/ drink / necessaries 
	--과자 snacks
	INTO BRAND VALUES (1, 'snacks','cheetos','lotte')
	INTO BRAND VALUES (2,'snacks','cornchip', 'crown' )
	INTO BRAND VALUES (3,'snacks','pringles', 'nongshim' )
	INTO BRAND VALUES (4,'snacks','vicpie', 'crown' )
	INTO BRAND VALUES (5,'snacks','zec', 'lotte' )
	INTO BRAND VALUES (6,'snacks','bananakick', 'nongshim' )
	INTO BRAND VALUES (7,'snacks','potatochip', 'nongshim' )
	INTO BRAND VALUES (8,'snacks','doritos', 'lotte' )
	INTO BRAND VALUES (9,'snacks','pepero', 'lotte' )
	INTO BRAND VALUES (10,'snacks','binch', 'lotte' )
	INTO BRAND VALUES (11,'snacks','kicker', 'crown' )
	INTO BRAND VALUES (12,'snacks','butterwaffle', 'crown' )
	INTO BRAND VALUES (13,'snacks','postick', 'nongshim' )
	INTO BRAND VALUES (14,'snacks','chocopie', 'crown' )
	-- 음료 beverage 
	INTO BRAND VALUES (15,'beverage','caprisun', 'nongshim' )
	INTO BRAND VALUES (16,'beverage','welch''s', 'nongshim' )
	INTO BRAND VALUES (17,'beverage','pepsi', 'lotte' )
	INTO BRAND VALUES (18,'beverage','milkiss', 'lotte' )
	INTO BRAND VALUES (19,'beverage','delmont', 'lotte' )
	INTO BRAND VALUES (20,'beverage','liptin', 'lotte' )
	INTO BRAND VALUES (21,'beverage','hotsix', 'lotte' )
	INTO BRAND VALUES (22,'beverage','pocarisweat', 'donga' )
	INTO BRAND VALUES (23,'beverage','demisoda', 'donga' )
	INTO BRAND VALUES (24,'beverage','narangd', 'donga' )
	INTO BRAND VALUES (25,'beverage','caprisun', 'nongshim' )
	--라면 ramen
	INTO BRAND VALUES (26,'ramen','shinramen', 'lotte' )
	INTO BRAND VALUES (27,'ramen','neoguri', 'lotte' )
	INTO BRAND VALUES (28,'ramen','jjapaghetti', 'lotte' )
	INTO BRAND VALUES (29,'ramen','jinramen', 'otoki' )
	INTO BRAND VALUES (30,'ramen','chamggae', 'otoki' )
	INTO BRAND VALUES (31,'ramen','yeulramen', 'otoki' )
	INTO BRAND VALUES (32,'ramen','ggoggomen', 'paldo' )
	--술 drink 
	INTO BRAND VALUES (33,'drink','jinro', 'hite' )
	INTO BRAND VALUES (34,'drink','chamisul', 'hite' )
	INTO BRAND VALUES (35,'drink','saero', 'lotte' )
	INTO BRAND VALUES (36,'drink','chueum', 'lotte' )
	INTO BRAND VALUES (37,'drink','hite', 'hite' )
	INTO BRAND VALUES (38,'drink','terra', 'hite' )
	INTO BRAND VALUES (39,'drink','cloud', 'lotte' )
	INTO BRAND VALUES (40,'drink','crush', 'lotte' )
	-- 담배 sigarette
	INTO BRAND VALUES (41,'sigarette','esse', 'kt&g' )
	INTO BRAND VALUES (42,'sigarette','theone', 'kt&g' )
	INTO BRAND VALUES (43,'sigarette','marlboro', 'Philip_Morris' )
	INTO BRAND VALUES (44,'sigarette','cammel', 'rjreynolds' )
	INTO BRAND VALUES (45,'sigarette','mevius', 'Japan_Tobacco' )
	INTO BRAND VALUES (46,'sigarette','sevenstar', 'Japan_Tobacco' )
	-- 생필품 necessaries 
	INTO BRAND VALUES  (47,'necessaries','kleenex', 'yuhankimberly' )
	INTO BRAND VALUES (48,'necessaries','poppy', 'yuhankimberly' )
	INTO BRAND VALUES (49,'necessaries','oralb', 'oralb' )
	INTO BRAND VALUES (50,'necessaries','dentimate', 'clio' )
	INTO BRAND VALUES (51,'necessaries','sensodyne', 'sensoodyne' )
	INTO BRAND VALUES (52,'necessaries','perio', 'lg' )
	INTO BRAND VALUES (53,'necessaries','elastine', 'lg' )
	INTO BRAND VALUES (54,'necessaries','kerasys', 'aekyung' )
	SELECT * FROM dual;
SELECT * FROM dual;

COMMIT;

SELECT * FROM teamprod;

SELECT * FROM history;

SELECT * FROM BRAND;