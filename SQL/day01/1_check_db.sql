-- SHOW 명령어 : 확인한다.

-- (1) 데이터베이스 목록 확인

SHOW DATABASES;

-- (2) 데이터베이스 선택
USE sakila;

SHOW Tables;

-- 테이블 생성시, 작성하 쿼리 원문 확인하기
-- 테이블 구조를 설계단에서 파악
SHOW CREATE TABLE sakila.actor;

-- 데이터 구조 파악하기
DESCRIBE actor;
DESC city;