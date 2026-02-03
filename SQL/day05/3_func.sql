USE world;
SELECT DATABASE();
-- 단일행 함수
-- [1] 문자열 함수
-- (1) CONCAT : 여러 문자열을 이어낸다

SELECT CONCAT(ct.Name, ' (',ct.`CountryCode`,')')
FROM city ct
WHERE ct.`CountryCode` IN (
    SELECT co.Code
    FROM country co
    WHERE co.Continent = 'Asia'
)

-- (2) SUBSTRING : 위치기반 특정 부분 잘라내기
SELECT co.Name, SUBSTRING(co.Name, 1, 3)
FROM country as co
LIMIT 5;

-- (3) LENGTH : 길이 반환
SELECT country.Name, LENGTH(country.Name) 문자길이
FROM country;

-- (4) REPLACE: 문자 대체
SELECT co.Name, REPLACE(co.Name,'South','S.')
FROM country co
WHERE co.Name LIKE '%South%';

-- [2] 숫자형 함수

SELECT co.`Name`, co.Population/co.SurfaceArea As 인구밀도, 
ROUND(co.Population/co.SurfaceArea, 2) As 반올림,
TRUNCATE(co.Population/co.SurfaceArea, 2) As 버림,
CEIL(co.Population/co.SurfaceArea) As 올림,
FLOOR(co.Population/co.SurfaceArea) As 내림
FROM country as co
WHERE co.Surfacearea > 0;

-- [3] 날짜형 함수
-- (1) 현재
SELECT NOW(), CURDATE(), CURTIME();
-- (2) 날짜 추출
SELECT HOUR(NOW());
SELECT WEEK(NOW());
SELECT YEARWEEK(NOW());

-- (3) 날짜 형식
SELECT DATE_FORMAT(NOW(), '%M-%Y');
-- 형식은 필요에 따라 찾아서 보면 된다.

-- (4) 날짜 연산
SELECT NOW() + 10; --의도 10일 뒤 => 분명하지 않음
SELECT DATE_ADD(NOW(), INTERVAL 10 DAY);
SELECT DATE_SUB(NOW(), INTERVAL 3 HOUR);

-- 예시 반납일 대여일 사이 간격 확인
USE sakila;
SELECT DATABASE();
SELECT AVG(DATEDIFF(r.return_date, r.rental_date)) as 대여기간
FROM rental r;

SELECT DATEDIFF('2026-03-27', CURDATE());

-- [4] NULL 관련 함수
-- 결측치 -> 비어 있는 값
DESC country;
use world;
SELECT COUNT(*)
FROM country
WHERE `HeadOfState` IS NULL;

-- (1) COALESCE, NULL 이 아닌 첫 번재 값을 반환
SELECT co.Name, co.GNPOld, co.GNP, COALESCE(co.GNPOld, co.GNP, 0) as 최종GNP
FROM country co;

-- (2) IFNULL, A가 NULL 아니면 A , NULL이면 B
SELECT co.Name, co.`HeadOfState`, IFNULL(co.`HeadOfState`, '정보없음') 결측치처리
FROM country as co
WHERE co.`Continent` = 'Europe'

-- (3) NULLIF, A와 B가 같으면 NULL을 반환하고, 다르면 A를 반환
SELECT cl.`Language`, cl.`Percentage`, NULLIF(cl.`Percentage`,0.0) 
FROM countrylanguage as cl
WHERE cl.`CountryCode` ='ANT'



--  다중행 함수
USE sakila;
SELECT
    ROUND(AVG(rental_rate),2),
    COUNT(*)
FROM

-- 실습 10
-- customer 테이블의 first_name과 last_name을 조합하여 표시용 full_name 컬럼을 만들어 보세요.
SELECT first_name 이름, last_name 성, CONCAT(first_name,' ',last_name) as full_name
FROM customer;

-- film 테이블에서 영화 제목(title)은 모두 대문자 설명(description)은 모두 소문자 로 변환하여 조회해 보세요.
SELECT UPPER(title) 영화제목, LOWER(description) 설명
FROM film

-- customer 테이블의 email 컬럼에서 @ 앞부분만 추출하여 사용자 ID 형태로 조회해 보세요.
SELECT SUBSTRING_INDEX(email,'@',1)
FROM customer;

-- payment 테이블의 결제 금액(amount)을 기준으로 각 처리 방식에 따른 결과를 한 번에 비교해 보세요.
SELECT 
ROUND(amount,1) as 반올림,
CEIL(amount) as 올림,
FLOOR(amount) as 내림
FROM payment

-- rental 테이블의 대여일(rental_date)을 YYYY-MM-DD (요일 약어) 형태로 변환하여 조회해 보세요.
SELECT DATE_FORMAT(rental_date, '%Y-%m-%d (%a)')
FROM rental;

-- rental 테이블과 payment 테이블을 활용하여 요일별 렌탈 건수 요일별 총 수익
SELECT 
DATE_FORMAT(r.rental_date, '%a')  요일별,
COUNT(*) 렌탈건수,
SUM(p.amount) 총수익
FROM rental r
JOIN payment p USING (rental_id)
GROUP BY DATE_FORMAT(r.rental_date, '%a');

-- rental 테이블의 대여일(rental_date)과 반납일(return_date)을 이용하여 각 대여 건의 실제 대여 기간(일수)을 계산해 보세요.
SELECT rental_id 고객번호, DATEDIFF(r.return_date, r.rental_date) as 대여기간 
FROM rental r;