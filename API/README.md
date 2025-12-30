# API 강의

> API 강의 진행 코드입니다.  
> 코드 자체를 외운다기 보다는 API 의 개념과 그 활용 측면에서 살펴보아 주세요 :) 

## 가상환경 설정
1. 생성하기
    ```bash
    python -m venv .venv   # .venv 폴더에 환경 생성
    ```
2. 활성화
    ```bash
    . .venv/Scripts/activate
    ```

3. 라이브러리 설치 및 사용
    ```bash
    python -m pip install requests
    ```

4. 비활성화
    ```bash
    deactivate
    ```

## API key 안전하게 다루기
1. 프로젝트 루트 디렉터리에 .env 파일을 생성합니다.
    ```bash
    touch .env
    ```

2. `.env` 파일내부에 다음과 같이 작성합니다.
    ```
    API_KEY=your_api_key_here
    ```

3. `.env` 파일을 Git 등 버전관리 시스템에 올리지 않으려면 .gitignore에 .env를 추가합니다.

4. 가상환경 내에서 `python-dotenv` 패키지를 설치합니다.
    ```bash
    python -m pip install python-dotenv
    ```

5. 파이썬 실습 코드에서 API key를 불러올 때, 반드시 다음과 같이 불러옵니다.
    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()  # .env 파일의 변수들을 환경변수로 등록
    api_key = os.getenv('API_KEY')  # 환경변수에서 API 키 불러오기

    print(api_key)  # 확인용, 실제 코드에서는 출력하지 않는 것이 안전
    ```

⭐️ API KEY 관리는 무척 중요합니다! ⭐️  
**⭐️ 보안 철저!⭐️**

> DAY01 (12/30)
1. API_basic => API 기초
2. API_TBMD => API 필터링 기초
3. gg => 공공데이터포털 API 활용