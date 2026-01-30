--  세 개 이상의 테이블 JOIN하기
USE world;
SELECT DATABASE();

-- world 데이터 베이스 예시
SELECT co.Name AS 국가명, ct.Name AS 수도명, cl.`Language` 
FROM 
    country AS co
    INNER JOIN
    city AS ct
    ON co.`Capital` = ct.ID  -- 수도의 케이스만 JOIN
    INNER JOIN
    countrylanguage AS cl
    ON cl.`CountryCode` = co.`Code`
WHERE cl.`IsOfficial` ='T';

-- sakila
USE sakila;
SELECT a.first_name 이름, a.last_name 성, f.title 영화이름
FROM
film f INNER JOIN film_actor fa
ON f.film_id = fa.film_id
INNER JOIN actor a
ON a.actor_id = fa.actor_id
LIMIT 5;

-- USING
USE sakila;
SELECT
a.first_name as 이름, a.last_name as 성, fa.title as 영화이름
FROM actor a INNER JOIN film_actor fa
USING (actor_id)