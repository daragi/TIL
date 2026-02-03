USE sakila;
SELECT DATABASE();
SHOW TABLES;
-- 데이터 형변환
-- [1] 암시적 형변환
SELECT '1' + 403;
-- 안되는 케이스
SELECT ct.category_id + CAST(ct.name as SIGNED)
FROM category ct;

-- [2] 명시적 형변환
SELECT CONCAT(CAST(ct.category_id as CHAR),'_',ct.name) as 형변환
FROM category as ct

SELECT YEAR(CAST(ct.last_update AS DATETIME))
FROM category as ct

SELECT CAST('2026' as YEAR)
FROM category as ct

SELECT CAST('2026' as YEAR) - YEAR(CAST(ct.last_update as DATETIME))
FROM category as ct;