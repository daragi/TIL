-- 윈도우 함수
-- 각 행의 개별 정보 유지 + 집계된 값을 붙이기
-- 행을 유지한채로 파티션별 추가 집계된 정보를 붙여서 '비교' 가능

SELECT
    co.Name,
    co.GNP,
    AVG(co.GNP) OVER(PARTITION BY co.`Continent`) as 대륙평균
FROM country co;

-- GROUP BY로 계산한 결과에 대해 JOIN하는 형태로 추가했던 이전방식보다
-- 훨씬 더 쉽고 간단하게 원본 행에 집계 값을 추가하여 표시할 수 있다.

-- [1] 누적합산
-- 아시아 국가들을 인구수를 기준으로 내림차순하고, 이들을 누적합 한다.
SELECT
    co.Name, co.Population,
    SUM(co.`Population`) OVER(ORDER BY co.`Population` DESC) as 인구누적합
FROM country co
WHERE co.`Continent` = 'Asia'

-- [2] 이동평균
SELECT
    co.Name,
    co.GNP,
    AVG(co.GNP) OVER(
        ORDER BY co.GNP
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) as 이동평균
FROM country as co
WHERE co.`Continent` = 'Europe'  -- 시계열 데이터에서 의미가있음

-- 다양한 윈도우 함수
-- [1] 순위
SELECT 
    co.Name,
    RANK() OVER(ORDER BY GNP DESC) as 순위,
    co.GNP
FROM country co; 

WITH scores AS (
    SELECT 'A학생' AS name, 95 AS score
    UNION ALL SELECT 'B학생', 90
    UNION ALL SELECT 'C학생', 85
    UNION ALL SELECT 'D학생', 85
    UNION ALL SELECT 'E학생', 85
    UNION ALL SELECT 'F학생', 70
)
SELECT
    name, score,
    ROW_NUMBER() OVER(ORDER BY score DESC) AS row_num,
    RANK()       OVER(ORDER BY score DESC) AS rnk,
    DENSE_RANK() OVER(ORDER BY score DESC) AS dense_rnk
FROM scores;

-- NTILE
SELECT
    co.Name,
    co.Continent,
    co.GNP,
    NTILE(4) OVER(ORDER BY co.GNP DESC) GNP티어
FROM country co

-- FIRST_VALUE, LAST_VALUE
SELECT co.Continent, 
    FIRST_VALUE(co.Name) OVER(
    PARTITION BY co.`Continent` ORDER BY co.`LifeExpectancy` DESC) 
    as 최고수명국가,
    LAST_VALUE(co.Name) OVER( 
        PARTITION BY co.Continent ORDER BY co.`LifeExpectancy` DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as 최저수명국가
FROM country as co
WHERE co.`LifeExpectancy` IS NOT NULL;

-- LAG(), LEAD() - 이전, 이후 (컬럼, N개 전후, 기본값)
SELECT 
    Name, LifeExpectancy,
    LAG(LifeExpectancy, 1, 0) OVER(ORDER BY LifeExpectancy DESC) 
    AS previous_country_le,
    LifeExpectancy - LAG(LifeExpectancy, 1, 0) OVER(ORDER BY LifeExpectancy DESC) 
    AS diff_with_previous
FROM country
WHERE Continent = 'Africa' AND LifeExpectancy IS NOT NULL
LIMIT 5;

-- 실습(12)
-- city 테이블에서 각 국가(CountryCode)별로 인구 기준 상위 5개 도시를 뽑아, 국가별 주요 도시 목록을 만들어 보세요.
WITH sort AS (
    SELECT
        CountryCode,
        Name ,
        Population,
        ROW_NUMBER() OVER (PARTITION BY CountryCode ORDER BY Population DESC) AS ranking
    FROM
        city
)
SELECT CountryCode, Name, Population 
FROM sort
WHERE ranking <= 5
ORDER BY CountryCode, Population DESC;