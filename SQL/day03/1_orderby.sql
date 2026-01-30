USE world;
SELECT DATABASE();
-- 1. 인구가 많은 순서대로 정렬
SELECT ct.Name AS 이름, ct.District AS 지역, ct. Population AS 인구
FROM city AS ct
ORDER BY ct.Population DESC;

SELECT ct.Name AS 이름, ct.District AS 지역, ct. Population AS 인구
FROM city AS ct
ORDER BY 인구 DESC;

-- 2. 여러 번 정렬
SELECT ct.Name, ct.CountryCode, ct.Population
FROM city AS ct
WHERE ct.CountryCode IN ('KOR','JPN','CHN')
ORDER BY ct.CountryCode, ct.Population DESC;

-- 3. NULL 값의 정렬
SELECT *
FROM country AS co
WHERE co.IndepYear IS NOT NULL AND co.IndepYear > 0
ORDER BY co.IndepYear;