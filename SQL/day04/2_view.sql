-- 자주 사용하는 쿼리 저장소
-- VIEW 객체
USE world;
SELECT DATABASE();

SHOW TABLES;

-- [1] VIEW 생성
-- 고정을 위한 가상테이블
-- 생성(DDL) -> CREATE
-- 아시아 대륙에 속한 국가들의 이름, 수도, 인구, GNP

CREATE VIEW asia_countries_view AS 
SELECT co.Name, co.`Capital`, co.`Population`, co.GNP
FROM country co INNER JOIN city ct
ON co.`Capital` = ct.`ID`
WHERE `Continent` = 'Asia'

SHOW TABLES;



SELECT * FROM asia_countries_view
WHERE `Population` < 100000000
ORDER BY `Population` LIMIT 10;

-- [2] VIEW 수정
CREATE OR REPLACE VIEW asia_countries_view AS
SELECT
    co.Code,
    co.Name AS country_name,
    ci.Name AS capital_name,
    co.Population AS country_population,
    co.GNP,
    co.GovernmentForm -- 컬럼 추가
FROM
    country co
JOIN
    city ci ON co.Capital = ci.ID
WHERE
    co.Continent = 'Asia';

-- [3] VIEW 삭제
DROP VIEW IF EXISTS asia_countries_view;

SHOW TABLES;