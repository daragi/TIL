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
