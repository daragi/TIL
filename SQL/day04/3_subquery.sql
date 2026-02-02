-- 데이터 반환 형태에 따른 서브쿼리
USE world;
SELECT DATABASE();

-- [1] 단일행 서브쿼리
-- 서브쿼리가 단일한 값 반환
-- 하나의 값 -> 비교 연산과 주로 사용된다.

-- 예시1. 평균 인구수보다 인구가 많은 도시 조회
SELECT Name, Population
FROM city 
WHERE `Population` > (SELECT AVG(Population) FROM city )

-- 예시2. 가장 많은 인구를 가진 도시의 국가 정보
SELECT *
FROM country as co
WHERE co.Code = (
    SELECT ct.CountryCode
    FROM city as ct
    ORDER BY ct.`Population` DESC
    LIMIT 1
)

-- [2] 다중행 서브쿼리
-- 여러값을 한번에 비교하기 어려워서 기준값x
-- IN, NOT IN, EXISTS 등 사용
-- 예시: English를 공식 언어로 사용하는 모든 국가의 이름을 조회하는 경우
SELECT cl.Countrycode
FROM countrylanguage as cl
WHERE cl.`Language` = 'English'
AND `IsOfficial` = 'T'

DESC country;
DESC countrylanguage;

-- [3] 다중컬럼 서브쿼리
SELECT bc.Name, bc.`Population`
FROM (
    SELECT ct.Name, ct.Population
    FROM city as ct
    WHERE ct.`Population` > 5000000
) as bc

-- 각 나라에서 가장 인구가 많은 도시의 정보를 조회하는 경우
SELECT ct1.Name, ct1.`CountryCode`, ct1.`Population`
FROM city as ct1
WHERE (ct1.`CountryCode`, ct1.`Population`) IN (
    SELECT ct2.`CountryCode`, MAX(ct2.`Population`)
    FROM city as ct2
    GROUP BY ct2.`CountryCode`
);

-- 실습 (7)
USE sakila;
SELECT DATABASE();
SHOW TABLES;

-- 전체 영화의 평균 대여료를 기준으로, 그보다 비싼 대여료를 가진 영화의 제목과 대여료를 조회하세요.
SELECT f.title, f.rental_rate
FROM film as f
WHERE f.rental_rate > 
(SELECT AVG(f.rental_rate) FROM film as f)

-- 해당 고객의 모든 결제 ID와 결제액을 조회하되, 전체 고객의 평균 결제액을 모든 행에 함께 표시하세요.
SELECT * FROM payment;
SELECT payment_id, amount, (SELECT AVG(amount) FROM payment) 평균결제액
FROM payment;

-- 먼저 ‘Action’ 카테고리에 속한 영화 ID 목록을 구한 뒤, 그 영화들에 해당하는 재고 정보만 inventory 테이블에서 조회하세요.
SELECT * FROM film;
SELECT film_id, inventory_id 
FROM inventory WHERE film_id IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name ='Action'
);

-- 캐나다에 속한 모든 도시를 기준으로, 그 도시들에 주소를 두고 있지 않은 고객의 이름을 조회하세요.
SELECT c.first_name as 이름, c.last_name as 성 
FROM customer as c
WHERE c.address_id IN (
    SELECT a.address_id 
    FROM address as a
    WHERE a.city_id NOT IN (
        SELECT ct.city_id
        FROM city as ct
        JOIN country as co ON ct.country_id = co.country_id
        WHERE co.country = 'Canada'
    ));
select * from customer;
select * from address;
select * from country;

/*
고객별로
지금까지의 총 결제 금액
고객당 평균 결제 금액
을 함께 계산한 뒤,
이를 고객 기본 정보와 결합하여 고객 이름 + 매출 요약 정보 형태의 리포트를 만들려고 합니다.
 
payment 테이블에서 고객별 결제 요약을 먼저 계산하고,
그 결과를 customer 테이블과 연결하여 조회하세요.

*/
SELECT c.first_name as 이름, c.last_name as 성, cal.total_spent, cal.avg_spent
FROM customer c
JOIN (
    SELECT customer_id, SUM(amount) as total_spent, AVG(amount) as avg_spent
    FROM payment
    GROUP BY customer_id) as cal
ON c.customer_id = cal.customer_id;

