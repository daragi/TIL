# Python Statistics Lab

### '*' 파일은 복습/연습문제 풀이

> 목표: 통계학 핵심 개념을 **Python 실습(NumPy / pandas / matplotlib / scipy / statsmodels)** 중심으로 정리하고,
> 매 단원마다 "개념 → 예제 → 실습 → 미니 과제" 흐름으로 학습합니다.

---

## 📌 환경 (선택)
- Python 3.10+
- numpy, pandas, matplotlib, scipy, statsmodels (필요 시 seaborn)
- Jupyter Notebook(.ipynb)

---

## 📂 디렉토리 구조(예시)


```text
.
├── day01/                 # 통계 기초 & 데이터 다루기: 표본/모집단, 요약통계, 시각화
├── day02/                 # 확률 기초: 확률변수, 기댓값/분산, 조건부확률, 베이즈
├── day03/                 # 분포: 이산/연속, 정규/이항/포아송 등, 중심극한정리
├── day04/                 # 추정: 점추정/구간추정, 신뢰구간, 표본크기
├── day05/                 # 가설검정: p-value, t-test/z-test, 카이제곱, ANOVA
├── day06/                 # 상관/회귀: 상관계수, 단순/다중회귀, 진단(잔차/다중공선성)
├── day07/                 # 비모수/리샘플링: 부트스트랩, 퍼뮤테이션, 윌콕슨 등
├── day08/                 # 실전 미니프로젝트: EDA → 가설 → 검정/모델링 → 리포트
└── data/                  # dataset
```
---
## 📚 상세 커리큘럼

> DAY01 (01/07)
1. stat_practice => 기술 통계에 대한 이해
2. 가설 설정 실습 => 귀무/대립 가설에 대한 이해
3. 가설 검정 실습 => 실제 상황에 따른 검정을 실습하고 이해
4. 가설 검정과 해석 => 애매한 상황에서 오류를 통제하며 검정

> DAY02 (01/08)
1. cheking_data => pandas 동작원리, 코드로 이해
2. start_colab => 데이터 로드 및 확인하기
   
> DAY03 (01/09)
1. choosing_data => pandas 데이터 추출, 선택
    * practice1 => 데이터 선택/추출 연습
2. data_update => 데이터 수정하기
    * practice2 => 데이터 수정 연습
  
> DAY04 (01/12)
1. basic_visualization => pandas 기본 시각화
2. preprocess => 결측치/이상치 처리