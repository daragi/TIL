-- 조건 분기와 전처리
-- [1] IF 함수

SELECT
co.Name, co.LifeExpectancy, IF(co.LifeExpectancy >= 80, '고령사회', '해당없음') 분류
FROM country as co
WHERE co.`Continent` ='Asia'

-- 다중 조건 불가능

-- [2] CASE 표힌식
-- like python if, elif, else
/*
CASE 
    WHEN 조건1 THEN 결과1  
    ELSE 조건2 THEN 결과2
    ELSE 기본값
END
*/
SELECT
    co.Name 국가명,
    co.Continent 대륙명,
    CASE
        WHEN co.Continent = 'Asia' THEN '아시아권'
        WHEN co.Continent = 'Europe' THEN '유럽권'
        ELSE '기타'
    END as 권역
FROM country as co;

DESC city;
DESC country;
DESC countrylanguage;
-- country 테이블에서 기대 수명(LifeExpectancy) 또는 경제 지표(GNP)가 누락된 국가들을 찾아 해당 국가와 대륙 정보를 함께 확인해 보세요.
SELECT co.Continent, co.Name, co.GNP, co.LifeExpectancy
FROM country co
WHERE `LifeExpectancy` IS NULL or GNP IS NULL;


-- 기대 수명(LifeExpectancy)이 NULL인 경우, 해당 국가가 속한 대륙 평균 기대 수명으로 보정한 값을 계산하고 원래 값과 대체 값을 함께 비교할 수 있도록 조회해 보세요.


SELECT c1.Name, c1.Continent, c1.`LifeExpectancy`, IFNULL(c1.LifeExpectancy, 평균수명) 결측치처리
FROM country as c1
JOIN (
    SELECT continent, ROUND(AVG(LifeExpectancy),1) as 평균수명
    FROM country 
    GROUP BY continent
) c2
ON c1.Continent = c2.Continent;

-- 'Republic'이라는 단어가 포함된 국가는 모두 Republic으로 통일하여 정규화된 정부 형태 컬럼을 만들어 보세요.
USE world;
SELECT Name, `GovernmentForm`,
CASE 
    WHEN `GovernmentForm` LIKE '%Republic%' THEN 'Republic' 
    ELSE GovernmentForm
END as gov
FROM country;

-- Population과 SurfaceArea를 활용하여 국가별 인구 밀도(1km²당 인구 수) 를 계산해 보세요.
SELECT Name, Population, SurfaceArea, ROUND((Population/ SurfaceArea),3) as 인구밀도
FROM country
WHERE `Population` > 0 AND `SurfaceArea` > 0;

-- 국가별 1인당 GNP를 계산하고, 국가명과 대륙 기준으로 비교 가능한 형태로 조회해 보세요. *GNP는 백만달러 단위 입니다.
SELECT * FROM country;
SELECT Name, Continent, ROUND((GNP * 1000000 / Population),2) as 1인당GNP
FROM country
WHERE GNP > 0
ORDER BY  1인당GNP DESC;

-- country 테이블의 전체 인구와 city 테이블의 수도 인구를 연결하여, 각 국가의 수도 인구 집중 비율(%) 을 계산해 보세요.
SELECT co.Name 국가, ct.Name 수도, ROUND((ct.`Population`/co.`Population`)*100,2) as '수도인구집중비율(%)'
FROM country co
JOIN city ct
ON co.`Capital` = ct.`ID`
WHERE ct.`Population` > 0 AND co.`Population` > 0;
