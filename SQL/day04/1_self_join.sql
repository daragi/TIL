-- Active: 1769560212430@@127.0.0.1@3306@world
-- 또다른 JOIN의 형태

-- SELF JOIN
-- 새로운 조인의 종류가 아닌 나 자신과의 연결

USE world;
SELECT DATABASE();

SELECT
    c2.Name AS Other_Country_On_Continent,
    c1.Continent
FROM
    country AS c1
INNER JOIN
    country AS c2 
    ON c1.Continent = c2.Continent
WHERE
    c1.Name = 'South Korea'
    AND c2.Name <> 'South Korea';
