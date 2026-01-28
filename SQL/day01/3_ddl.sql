-- DDL : 데이터 구조 정의

-- [1] CREATE 생성
SHOW DATABASES;
-- (1) 데이터베이스 생성
CREATE DATABASE lecture;
SHOW DATABASES;

-- (2) 테이블 생성
USE lecture;
CREATE TABLE user (
    user_id INT PRIMARY KEY, -- 기본키
    name VARCHAR(50),
    email VARCHAR(100));

SHOW TABLES;

-- [2] ALTER : 변경
-- (1) 추가
ALTER TABLE `user`
ADD birthday DATE NOT NULL;

DESCRIBE user;

-- (2) 수정
ALTER TABLE `user`
MODIFY name VARCHAR(20) NOT NULL;

DESCRIBE user;

-- (3) 삭제
CREATE TABLE test (
    id INT PRIMARY KEY,
    name VARCHAR(20)
);
DROP TABLE test;

-- 있는 경우에만 삭제
DROP TABLE IF EXISTS test;

-- (4) 이름 변경
RENAME TABLE users TO user_info;