# 🤖 Machine Learning

데이터 기반 예측 문제를 해결하기 위한  
**머신러닝 모델링 및 성능 개선 과정**을 학습합니다.

---

## 📌 Learning Objective

- 지도학습 / 비지도학습 기본 개념 이해
- 분류 / 회귀 모델 실습
- Feature Engineering 적용
- 모델 성능 평가 지표 학습  
  (Accuracy, Precision, Recall, F1, ROC-AUC)
- Ensemble 기반 성능 개선
- Data Mining 기법 활용
- 모델 최적화 및 Hyper Parameter Tuning

➡ 데이터 전처리 → 모델링 → 평가 → 개선 흐름 중심으로 학습

---

# 📂 Contents

## 1. Machine Learning Pipeline

### 핵심 학습 내용
- Pipeline 구조 이해
- `GridSearchCV`와 결합한 자동화 학습
- `ColumnTransformer` 활용 전처리 통합
- 전처리 + 모델링 + 평가 일괄 구성

### 실습 파일
- `preprocess.ipynb`

---

## 2. Feature Engineering

### 세부 학습 내용

### 2-1. Encoding

#### 순서가 있는 범주형 변수
- Ordinal Encoding

#### 순서가 없는 범주형 변수
- Label Encoding
- One-Hot Encoding

### 2-2. Scaling

- StandardScaler
- MinMaxScaler
- RobustScaler

### 2-3. Feature Transformation

- 구간화 (Binning)
- 수학적 변환
- 로그 변환
- 날짜 파생 변수 생성
- 불필요 Feature 제거

---

## 3. Regression

## 선형 회귀
- sklearn 기반 선형 회귀 구현
- statsmodels 기반 회귀 해석

## 다중 선형 회귀
- 다중 변수 회귀 모델 구성
- 다중공선성(VIF) 확인

## 실습 파일
- `regression.ipynb`
- `regression_practice.ipynb`

---

## 4. Classification

### 기본 분류 모델

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

### 실습 분류 문제 해결

- 학습 / 테스트 데이터 분리
- 기준선 모델 구성
- class_weight 적용
- SMOTE 오버샘플링

### 평가 지표

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

## 5. Hyper Parameter Tuning

### 학습 내용

- Grid Search
- 하이퍼파라미터 튜닝 전략
- 과적합 / 과소적합 비교
- 최적 모델 선택

### 실습 파일
- `hyper_parameter.ipynb`

---

## 6. Ensemble Learning

### 모델 결합 방식

- Random Forest
- XGBoost
- Voting Ensemble
- Bagging / Boosting 개념

### 실습 파일
- `ensemble.ipynb`

---

## 7. Data Mining

### 차원 축소 / 해석

- PCA
- Feature Importance
- SHAP

### 군집 분석

- K-Means Clustering

### 실습 파일
- `data_mining.ipynb`

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Matplotlib
- Seaborn

---

# 📈 Learning Flow

```text
Data Preprocessing
→ Feature Engineering
→ Model Training
→ Evaluation
→ Performance Improvement
→ Interpretation