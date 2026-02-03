```
매일 SQL을 학습하며 기록하는 공간입니다.  
실전에서 자주 쓰이는 SELECT 문법부터 집계, 조인, 서브쿼리, 윈도우 함수까지  
**개념 → 예제 → 실습 → 미니 과제** 흐름으로 정리합니다.
```
---

## 📌 환경

- MySQL + VisualStudio Code
- MySQL Workbench
- Jupyter Notebook + `ipython-sql` (선택)

---

## 📂 디렉토리 구조 (예시)

```text
.
├── day01/                     # SQL 기본 문법 & SELECT, FROM, WHERE
├── day02/                     # 데이터 정렬, 조건문, NULL 처리
├── day03/                     # GROUP BY, HAVING, 집계 함수
├── day04/                     # JOIN: INNER / LEFT / RIGHT / FULL
├── day05/                     # Subquery & Derived Table
├── day06/                     # Window Functions (OVER, PARTITION, RANK 등)
├── day07/                     # 문자열 함수, 날짜 함수, 형 변환
├── day08/                     # 데이터 모델링 & ERD 실습 (보너스)
└── data/                      # 실습용 Sample DB (ex. employees, e-commerce, sns)
```
---
## 📚 상세 커리큘럼

> DAY01 (01/28)
1. 1_check_db.sql => `SHOW`, `DESCRIBE` 문법 숙지
2. 2_sql_intro.sql => SQL 기본 사용법
3. 3_ddl.sql => DDL 기초 (`CREATE`, `ALTER`, `DROP`, `MODIFY`)
4. 4_dml.sql => DML 기초 (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
* day01_practice => DDL/DML 연습

> DAY02 (01/29)
* day01_wrapup => `DDL`, `DML` 복습
1. 1_select => `SELECT` 기본
2. 2_select_logic => `SELECT` 처리
3. 3_where => `WHERE` 조건문
4. 4_groupby => 집계
5. 5_having => 집계 조건문

> DAY03 (01/30)
* day02_wrapup => `SELECT` , `GROUP BY` 복습
1. 1_orderby.sql => 정렬
2. 2_join_basic.sql => 테이블 `join`
3. 3_join_adv.sql => 테이블 `join` 심화

> DAY04 (02/02)
* day03_wrapup => join 복습
1. 1_self_join.sql => `SELF JOIN` 예제
2. 2_view.sql => `VIEW` 생성/수정/삭제
3. 3_subquery.sql => 서브쿼리
4. 4_subquery_corr.sql => 연관/비연관 서브쿼리

> DAY05 (02/03)
* day04_wrapup => 서브쿼리 복습
1. 1_cte => 서브쿼리 대체문 `CTE` 학습