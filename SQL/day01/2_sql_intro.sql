-- SQL의 특징
-- 쿼리가 끝났음을 알리는 세미콜론 (;)
USE world;
SHOW TABLES;

-- (2) 대소문자 구분
-- 대소문자 구분하지 않지만 가독성을 위해 구분
SELECT *
FROM city
LIMIT 5;

select * from city limit 5;

-- (3) 주석
-- ctrl + / : 한줄 주석
SELECT c.`Name`, c.`District`, c.`Population`
FROM city AS c
WHERE c.`Population` > 10000000;

/*
여러 줄
주석도
가능합니다.
*/

-- (4) 정렬과 띄어쓰기
-- 공백 갯수와 쿼리 값의 결과는 무관
select * from city limit 5;