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

-- 실습(6)
USE sakila;
SELECT DATABASE();

-- customer, address, city 세 개의 테이블을 연결하여 고객의 기본 정보, 주소, 도시 이름을 한 번에 조회해 보세요.
DESC customer;
DESC address;
DESC city;
SELECT c.first_name 이름, c.last_name 성, a.address 주소, ct.city 도시명
FROM 
customer c INNER JOIN address a
USING (address_id)
INNER JOIN city ct
USING (city_id)

-- customer, address, city 테이블을 JOIN하여 London에 거주하는 고객들의 기본 정보, 주소, 도시를 조회해 보세요.
SELECT c.first_name 이름, c.last_name 성, a.address 주소, ct.city 도시명
FROM
customer c INNER JOIN address a
USING (address_id)
INNER JOIN city ct
USING (city_id)
WHERE ct.city = 'London'

/*
customer, address, city 테이블을 JOIN하여 각 도시에 몇 명의 고객이 살고 있는지 계산해 보세요.
고객 수가 많은 순서대로 정렬(ORDER BY)하여 결과를 확인해 보세요.
운영 리포트에서는
“어느 도시에 고객이 많이 분포되어 있는가”를 자주 확인합니다.
customer, address, city 테이블을 JOIN하여
도시별 고객 수를 계산하고,
고객 수가 많은 순서대로 정렬해 보세요.
*/
SELECT ct.city 도시명, COUNT(*) 고객수
FROM
customer c LEFT JOIN address a
USING (address_id)
LEFT JOIN city ct
USING (city_id)
GROUP BY ct.city
ORDER BY COUNT(*) DESC;

DESC country;
DESC city;

SELECT co.country 나라명, ct.city 도시명, a.address 주소
FROM
customer c INNER JOIN address a
USING (address_id)
INNER JOIN city ct
USING (city_id)
INNER JOIN country co
USING (country_id)

-- 세 테이블을 JOIN하여 각 배우의 이름과 출연 영화 제목을 조회해 보세요.
USE sakila;
SHOW TABLES;
DESC actor;
DESC film;
DESC film_actor;
SELECT a.first_name 이름, a.last_name 성, f.title 영화제목
FROM
actor a INNER JOIN film_actor fa
USING (actor_id)
INNER JOIN film f
USING (film_id)

-- 배우의 first_name이 PENELOPE인 경우에 한해, 그 배우가 출연한 영화 제목을 조회해 보세요.
SELECT a.first_name 이름, a.last_name 성, f.title 영화제목
FROM
actor a INNER JOIN film_actor fa
USING (actor_id)
INNER JOIN film f
USING (film_id)
WHERE a.first_name = 'PENELOPE'