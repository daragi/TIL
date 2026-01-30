-- ======= SELECT =======
USE world;
SELECT DATABASE(); -- 현재 내가 보고 있는 데이터베이스의 이름 확인
SHOW TABLES;
DESC city;
SELECT Name, CountryCode, Population
FROM city;
SELECT ct.Name, ct.CountryCode, ct.Population
FROM city AS ct;

SELECT
city.Name AS 도시명,
city.CountryCode AS 국가코드,
city.Population AS 인구수
FROM city;
SELECT co.Continent AS 대륙별, COUNT(*) AS 나라수
FROM country AS co
GROUP BY co.Continent;
SELECT ct.Name AS 도시명, ct.CountryCode AS 국가코드, ct.Population AS 인구수
FROM city AS ct
WHERE ct.CountryCode = 'KOR'

-- country 테이블에서 대륙별로 정렬하고, 같은 대륙 내에서는 GNP가 높은 순으로 정렬하여 Name, Continent, GNP을 조회하세요.
SELECT ct.Name, ct.Continent, ct.GNP
FROM country AS ct
ORDER BY Continent, GNP DESC;

-- 대륙 별 국가 수가 많은 순서대로 Continent, 국가 수를 조회하세요.
SELECT Continent, COUNT(*) AS 국가수
FROM country
GROUP BY Continent
ORDER BY COUNT(*) DESC;

-- 독립년도가 있는 국가들의 대륙 별 평균 기대수명이 높은 순서대로 Continent, 평균 기대수명을 조회하세요.
SELECT Continent, AVG(LifeExpectancy) AS 평균기대수명
FROM country
WHERE `IndepYear` IS NOT NULL
GROUP BY `Continent`
ORDER BY AVG(`LifeExpectancy`) DESC;

-- 인구가 많은 도시 중 11위부터 20위까지 조회하세요.
SELECT * FROM city
ORDER BY Population DESC
LIMIT 10 OFFSET 10;

