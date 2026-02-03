-- CTE
-- WITH 절을 통해, 해당 쿼리에서만 사용할 임시뷰를 선언하는 방식

-- 예시 : 각 대륙에서 인구가 가장 많은 국가 찾기
-- 1. 서브쿼리 사용
SELECT c1.Continent, c1.Name, c1.Population
FROM country as c1
JOIN (
    SELECT c2.Continent, MAX(c2.`Population`) AS max_pop
    FROM country as c2
    GROUP BY c2.Continent
) as cmp
ON cmp.Continent = c1.`Continent` 
AND
cmp.max_pop = c1.`Population`

-- CTE 사용
WITH cmp AS (
    SELECT `Continent`, MAX(Population) as max_pop
    FROM country
    GROUP BY Continent
)
SELECT c.`Continent`, c.`Name`, c.`Population`
FROM country as c
INNER JOIN cmp
ON c.Continent = cmp.`Continent` AND c.`Population` = cmp.max_pop

-- 실습 9
USE sakila;
SELECT DATABASE();
SHOW TABLES;

-- 아래 서브쿼리 예시를 참고하여, 동일한 결과가 나오도록 CTE로 변환해 보세요.
/*
SELECT c.first_name, c.last_name
FROM customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film_category fc ON i.film_id = fc.film_id
    JOIN category cat ON fc.category_id = cat.category_id
    WHERE r.customer_id = c.customer_id
    AND cat.name = 'Action'
);
*/

WITH norental as (
    SELECT DISTINCT r.customer_id
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film_category fc ON i.film_id = fc.film_id
    JOIN category ct ON fc.category_id = ct.category_id
    WHERE ct.name = 'Action'
)
SELECT c.first_name 이름, c.last_name 성
FROM customer c
LEFT JOIN norental ON c.customer_id = norental.customer_id
WHERE norental.customer_id IS NULL;

/*
아래 서브쿼리 예시를 참고하여, 동일한 결과가 나오도록 CTE로 변환해 보세요.
SELECT DISTINCT f.title
FROM film f
WHERE f.film_id IN (
    SELECT i.film_id
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    WHERE r.customer_id IN (
        SELECT customer_id
        FROM rental
        GROUP BY customer_id
        HAVING COUNT(*) >= 40
    )
);
*/

WITH Top AS (
    SELECT customer_id
    FROM rental
    GROUP BY customer_id
    HAVING COUNT(*) >= 40
),
Movie AS (
    SELECT DISTINCT film_id
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    WHERE r.customer_id IN(
        SELECT customer_id
        FROM Top
    )
)
SELECT f.title
FROM film f
JOIN Movie ON f.film_id = Movie.film_id;