-- JOIN으로 여러 테이블 연결하기

-- [1] INNER JOIN
-- 1: N 관계
DESC Country;
SELECT city.Name AS 도시명, country.Name AS 국가명, country.`Continent` AS 대륙명
    FROM 
    city
    INNER JOIN
    country
    ON city.`CountryCode` = country.`Code`

-- [2] LEFT JOIN

SELECT 
co.Name as 나라명,
ct.Name as 수도명,
ct.Population as 도시,
ct.District as 지역
FROM country as co
LEFT JOIN city as ct
ON co.`Capital` =ct.`ID`

-- sakila 비디오 대여점 예씨
USE sakila;
SHOW TABLES;
DESC rental;
DESC customer;

-- 질문: 고객의 대여내역(대여일자, 반납일자) 정보를 보고 싶다.
-- 대상 테이블
    -- 고객 customer
    -- 대여내역 rental
-- 우리는 자세히 무엇을 원하는가?
    -- 1) 모든 고객 -> LEFT
    -- 2) 대여를 한번이라도 해본 고객을 보기 원하는가? -> INNER
SELECT
c.first_name, c.last_name, r.rental_date, r.return_date
FROM
    customer AS c
    LEFT JOIN
    rental AS r
    ON c.customer_id = r.customer_id

SELECT
c.first_name, c.last_name, r.rental_date, r.return_date
FROM
    customer AS c
    LEFT JOIN
    rental AS r
    ON c.customer_id = r.customer_id
    WHERE r.rental_date IS NULL;
USE sakila;
SELECT DATABASE();
SHOW TABLES;

-- customer 테이블과 address 테이블을 INNER JOIN하여, 각 고객의 이름(first_name, last_name)과 주소(address)를 함께 조회해 보세요. 
-- 두 테이블은 address_id로 연결됩니다.
SELECT c.first_name, c.last_name, a.address
FROM 
customer c INNER JOIN address a
ON c.address_id = a.address_id

-- film 테이블과 language 테이블을 조인하세요. 각 영화의 제목(title)과 해당 영화의 언어 이름(name)을 조회하는 쿼리를 작성합니다.
-- 공통 컬럼은 language_id 입니다.
SELECT f.title, l.name
FROM
film f JOIN language l
ON f.language_id = l.language_id

-- customer 테이블을 기준으로 rental 테이블을 LEFT JOIN 하세요.
-- 모든 고객의 이름을 조회하되, 각 고객이 마지막으로 대여한 날짜(rental_date)를 함께 표시해야 합니다.
DESC customer;
DESC rental;

SELECT c.first_name, c.last_name, MAX(r.rental_date) as last_date
FROM customer c LEFT JOIN rental r
ON c.customer_id = r.customer_id
GROUP BY c.customer_id

-- customer 테이블과 address 테이블을 조인한 후, city_id가 312인 도시에 거주하는 고객의 이름과 이메일을 찾아보세요.
SELECT c.first_name, c.last_name, c.email
FROM 
customer c JOIN address a
ON c.address_id = a.address_id
WHERE a.city_id = 312;

-- staff 테이블과 payment 테이블을 조인하여, 각 직원의 이름(first_name)과 그 직원이 처리한 총 결제 건수를 조회하세요.
DESC staff;
DESC payment;
SELECT s.first_name, COUNT(p.payment_id) 총결제건수
FROM staff s JOIN payment p
ON s.staff_id = p.staff_id
GROUP BY s.staff_id;

-- customer 테이블과 payment 테이블을 조인하여 고객별로 총 결제액(amount)을 계산하세요. 그중 총 결제액이 $180 이상인 우수 고객의 이름과 총 결제액을 조회하세요.
SELECT c.first_name, c.last_name, SUM(p.amount) 총결제액
FROM customer c JOIN payment p
ON c.customer_id = p.customer_id
GROUP BY c.customer_id
HAVING 총결제액 >= 180
ORDER BY 총결제액 DESC;