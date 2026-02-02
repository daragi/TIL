-- 동장 방식에 따른 서브쿼리
USE sakila;
SELECT DATABASE();
-- [1] 비연관 서브쿼리
-- 메인쿼리와 연관이 없다 -> 메인쿼리 없이도 서브쿼리가 잘 실행된다.
-- 실행 순서 : 서브쿼리 -> 메인쿼리
    --  한번에 끝!
SELECT f.title
FROM film f
WHERE f.film_id IN(
    SELECT DISTINCT i.film_id
    FROM rental r
    JOIN inventory i
    ON r.inventory_id = i.inventory_id
);

-- [2] 연관 서브쿼리
-- 메인쿼리와 연관이 있다 -> 메인쿼리 없이 서브쿼리는 실행될 수 없다.
    -- why? 서브쿼리 안에서 메인쿼리의 값을 사용
-- 실행 순서 : 메인쿼리 -> 서브쿼리 실행 -> 메인쿼리 사용
    -- 메인쿼리의 모든 행에 대해서 반복
SELECT f.title
FROM film as f
WHERE EXISTS (
    SELECT 1 
    FROM rental as r
    JOIN inventory as i
    ON r.inventory_id = i.inventory_id
    WHERE f.film_id = i.film_id
);

-- 실습 (8)
-- ‘Action’ 카테고리에 속한 모든 영화의 제목(title)과 설명(description)을 조회해 보세요.
SELECT f.title, f.description
FROM film as f
WHERE f.film_id IN (
    SELECT fc.film_id
    FROM film_category as fc
    JOIN category as c
    ON fc.category_id = c.category_id
    WHERE c.Name = 'Action'
);

-- 연관 서브쿼리를 사용하여 각 고객의 이름(first_name, last_name)과 해당 고객의 가장 최근 대여일(rental_date)을 조회해 보세요.
SELECT c.first_name 이름, c.last_name 성, (
    SELECT MAX(r.rental_date) 
    FROM rental as r
    WHERE r.customer_id = c.customer_id) 최근대여일
FROM customer as c
-- GROUP BY c.customer_id

-- 고객 한 명씩 확인하면서 Horror 영화 대여 기록이 존재하는지만 검사하도록 EXISTS를 사용하는 연관 서브쿼리로 
-- 조건을 만족하는 고객의 이름(first_name, last_name)을 조회해 보세요.
SELECT c.first_name, c.last_name
FROM customer as c
WHERE EXISTS (
    SELECT 1
    FROM rental as r
    JOIN inventory as i ON r.inventory_id = i.inventory_id
    JOIN film as f ON i.film_id = f.film_id
    JOIN film_category as fc ON f.film_id = fc.film_id
    JOIN category as ca ON fc.category_id = ca.category_id
    WHERE ca.Name = 'Horror' AND r.customer_id = c.customer_id
);