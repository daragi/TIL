DESC user_info;

SELECT * FROM user_info;

-- DML : 데이터 조작
-- [1] INSERT : 데이터 삽입
-- (1) 단일행 삽입
INSERT INTO user_info(user_id,name,email,birthday)
VALUES (101, 'alex', 'alex@example.com', '2002.01.01');

SELECT * FROM user_info;

-- (2) 다중행 삽입
INSERT INTO user_info(user_id, name, email, birthday)
VALUES
(102,'jun', 'jun@example.com', '1996.10.30'),
(103,'chelsea', 'chelsea@example.com', '1990.01.20');

SELECT  * FROM user_info;

-- 혹시 결측이 있어도 될까?
INSERT INTO user_info(user_id,name,email,birthday)
VALUES (104, 'ken',NULL,'2000.04.18');

-- DESC에 NOT NULL 조항이 없으면 가능
INSERT INTO user_info(user_id,name,birthday)
VALUES (105, 'hobby','1999.01.13');

DESC user_info;