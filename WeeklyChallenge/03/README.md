# [위클리 챌린지] 3주차

## 📋 과제


1. NumPy 배열 생성 및 연산 문제 풀기: 모든 미니퀘스트 수행(노트북 파일 1개)
2. Pandas를 활용한 데이터 처리 문제 풀기: 모든 미니퀘스트 수행(노트북 파일 1개)
   1. 데이터를 pandas DataFrame으로 만들고, groupby 기능을 사용해보세요.
   2. 데이터를 DataFrame으로 만들고, 특정 조건을 필터링한 DataFrame을 만드세요.
3. 데이터 시각화의 모든 미니 퀘스트 수행(노트북 파일 1개)
   1. 시계열 데이터를 입수하여 시각화하세요.
   2. (선택) 양자 회로의 실행 결과를 시각화하세요.


## 📢 설명

1. NumPy 배열 생성 및 연산 문제 풀기
    - [x] NumPy 모든 미니퀘스트 수행
2. Pandas 활용한 데이터 처리 문제 풀기
    - [x] Pandas 모든 미니퀘스트 수행
    - [x] 데이터를 pandas DataFrame으로 만들고, groupby 기능 사용해보기
    - [x] 데이터를 DataFrame으로 만들고, 특정 조건을 필터링한 DataFrame 만들기
3. 데이터 시각화 문제 풀기
    - [x] 데이터 시각화 모든 미니퀘스트 수행
    - [x] 시계열 데이터를 입수해 시각화하기
    - [ ] (선택) 양자 회로의 실행 결과 시각화하기

| 기능 | 설명 |
|---|---|
| 기능 | 1. NumPy: Dimension, Shape, Data Type, Indexing, Operation, Universal Function<br>2. Pandas: Series, DataFrame<br>3. Data Visualization: Structured Data, Unstructured Data, Matplotlib, Seaborn, Time Series Data, SciPy |
| 추가<br>목표 | 1. 양자 회로의 실행 결과 시각화하기 |

#### 링크
> `.ipynb` 파일이 깃허브에서 열리지 않는다면

1. [NumPy 배열 생성/연산 문제 풀기](https://colab.research.google.com/drive/12CXxeN_G5XOsGza40W53gaBR20befUld?usp=sharing)
2. [Pandas 활용 데이터 처리 문제 풀기](https://colab.research.google.com/drive/1S8mHF5vfZRaRFzc2C4tW6mXhoi9IcR8-?usp=sharing)
3. [데이터 시각화 문제 풀기](https://colab.research.google.com/drive/19q85VT-wQgKYngEfsS5bRJ0jDZiuNUt-?usp=sharing)
4. [실제 데이터 처리](https://colab.research.google.com/drive/1QwvTJF16b-rHrj-OWr2xyZHDuDy5w32M?usp=sharing)
5. [시계열 데이터 시각화](https://colab.research.google.com/drive/1LH9vfjxHgoAVJYm5oNi1yiz9JM8S2GXU?usp=sharing)


### 1) 데이터 `groupby` 기능 사용 및 조건 필터링

#### 사용한 데이터
[행정안전부_통계연보_지역안전등급](https://www.data.go.kr/data/15077976/openapi.do)

#### 지역안전등급 데이터

> 지역별 안전 수준을 교통사고, 화재, 범죄 등의 통계로 수치화한 것
>   - 교통사고, 화재, 범죄, 생활안전, 자살, 감염병
>   - 1등급(가장 안전) - 5등급(가장 위험)


#### 지역안전등급 데이터 JSON 구조
```text
RegionalSafetyGrade
├── [0] : head (메타데이터)
└── [1] : row (실제 데이터)
```

#### 요청 데이터 형식
<img width="1214" height="330" alt="image" src="https://github.com/user-attachments/assets/72795313-d782-4624-827a-0c118d3f9e18" />

#### 출력 데이터 형식
<img width="1219" height="789" alt="image" src="https://github.com/user-attachments/assets/54eb1413-fe43-4622-9558-bff426fdfe5b" />

### 2) 시계열 데이터 입수해 시각화

#### 사용한 데이터
[HuggingFace ppg-bp-dataset](https://huggingface.co/datasets/SH36/ppg-bp-dataset/tree/main)

#### SBP / DBP

| 용어 | 설명 | 정상 범위 | 고혈압 위험 |
|---|---|---|---|
| SBP(Systolic Blood Pressure) | 수축기 혈압<br>심장이 수축하면서 혈액을 내보낼 때의 최대 압력 | 90 - 120 mmHg | 140 이상 |
| DBP(Diastolic Blood Pressure) | 이완기 혈압<br>심장이 쉬는 동안의 혈압 | 60 - 80 mmHg | 90 이상 |

#### PPG 데이터
- Photoplethysmography
- 빛을 피부에 비추어 **'혈류 변화'**를 측정하는 기술
- 원리
  - 혈액량 많아지면 -> 빛 흡수 ↑
  - 혈액량 적어지면 -> 빛 흡수 ↑
  ```text
    LED -> 혈관 -> 반사되는 빛
  ```
- PPG와 혈압의 관계
  - 혈압과 밀접한 관계
    - 혈관 상태
    - 혈류량
    - 맥파 형태
  - 변화 발생
  ```text
    혈압 상승 -> 혈관 탄성 변화 -> PPG 파형 변화
  ```
  - AI 모델
  ```text
    PPG 파형 -> CNN -> SBP/DBP 예측
  ```


## 🚀 사용법

### 1) 데이터 `groupby` 기능 사용 및 조건 필터링

```bash
# 1. 공공데이터포털에서 행정안전부_통계연보_지역안전등급 데이터 신청

# 2. 데이터 URL, KEY 값 env.text에 저장
REGIONAL_SAFETY_GRADE_URL=행정안전부_통계연보_지역안전등급 url
REGIONAL_URL_SERVICE_KEY=행정안전부_통계연보_지역안전등급 신청한 후 받은 키 값

# 3. colab에서 Google Drive 마운트
drive.mount('/content/drive')
env_file_path = '/content/drive/MyDrive/ColabNotebooks/kakao/env.text'

# 4. 데이터 불러오기
url = api_url

# 요청 변수 (Request Parameter)
#   서비스키, 페이지 번호, 한 페이지 결과 수, 호출문서
params = {
    "serviceKey": api_key,
    "pageNo": 1,
    "numOfRows": 100,
    "type": "json"
}

response = requests.get(url, params=params)
data = response.json()
```

#### 폴더링
```text
colab 폴더/
├── env.text
└── analysis-practice.ipynb
```


### 2) 시계열 데이터 입수해 시각화
```bash
# 1. huggingFace에서 PPG 데이터 다운받고 업로드

# 2. colab에서 Google Drive 마운트
drive.mount('/content/drive')
ppg_tar_path = '/content/drive/MyDrive/ColabNotebooks/kakao/ppg-bp-dataset.tar.gz' # 압축 파일 경로
extract_path = "/content/ppg-bp-dataset"# 압축 해제

# 3. 데이터 변환
# 숫자형 변환
df["SBP"] = pd.to_numeric(df["SBP"])
df["DBP"] = pd.to_numeric(df["DBP"])

# 샘플 순서를 시간축처럼 사용
df["time_index"] = range(len(df))

# 4. PPG 데이터로부터 추출된 혈압 라벨(SBP, DBP)이 샘플 순서에 따라 어떻게 변하는지 시각화
```

#### 폴더링
```text
colab 폴더/
├── ppg-bp-dataset.tar.gz
└── time-series-data.ipynb
```

## 💻 실행 예시

### 1) 데이터 `groupby` 기능 사용 및 조건 필터링

#### 데이터 그룹화
```bash
# 지역 기준으로 데이터 그룹화 & 범죄 등급 컬럼만 선택
grouped_crim = df.groupby("regi")["crim"].mean()
```

```dataframe
regi
강원    3.666667
경기    3.333333
경남    3.000000
경북    1.666667
광주    3.166667
대구    2.333333
대전    3.833333
부산    4.333333
서울    4.666667
세종    1.000000
울산    2.000000
인천    2.666667
전남    1.833333
전북    1.666667
제주    5.000000
충남    2.833333
충북    3.833333
Name: crim, dtype: float64
```

#### 데이터 조건 필터링
```bash
# 조건: 범죄 등급 평균 4 이상 & 교통사고 등급 평균 2 이상 & 화재 등급 평균 2 이상
filtered = df.groupby("regi").filter(lambda x: (x['crim'].mean() >= 4) & (x['trffac'].mean() >= 2) & (x['fire'].mean() >= 2))
```

```dataframe
   bas_yy regi  trffac  fire  crim  natdsast  comu_safe  suicid  infect
1    2016   부산       2     3     4         5          1       5       5
18   2017   부산       2     4     4         3          2       5       5
35   2018   부산       2     4     4         2          1       5       4
52   2019   부산       2     2     4         0          1       5       4
69   2020   부산       2     3     5         0          1       5       5
86   2021   부산       2     3     5         0          3       5       3
```


### 2) 시계열 데이터 입수해 시각화

#### SBP, DBP 데이터 시각화
```text
PPG 데이터로부터 추출된 혈압 라벨(SBP, DBP)이 샘플 순서에 따라 어떻게 변하는지 시각화
SBP (수축기 혈압) / DBP (이완기 혈압)
```

<img width="1002" height="544" alt="image" src="https://github.com/user-attachments/assets/5e7b08df-d3e1-4cd5-8ef9-6fd900c61f25" />



## 📁 파일 구조

```text
02/
├── data/
│   ├── env.text
│   └── ppg-bp-dataset.tar.gz
├── .gitignore
├── data_visualization.ipynb
├── dataframe_practice
├── numpy.ipynb
├── pandas.ipynb
└── time_series_data.ipynb
```

## 📝 회고
이번 과제를 진행하며 
- 배운점
  - 이번 데이터 분석 및 시각화 실습에서는 최대한 AI의 도움을 받지 않고 직접 코드를 작성하고자 노력했습니다. Pandas를 활용한 DataFrame 생성, 데이터 전처리, groupby를 이용한 데이터 집계, 조건 필터링, Matplotlib를 이용한 시각화 과정을 수행하며 데이터 분석의 기본 흐름을 익힐 수 있었습니다.
  - 실제 공공데이터와 의료 데이터를 직접 활용해보며 데이터의 구조를 파악하고 적절한 분석 방법을 선택하는 과정이 중요함을 배웠습니다.
- 고민점
  - 이번 실습에서 가장 고민했던 부분은 어떤 데이터를 활용할 것인가 였습니다. 특히 지역안전등급 데이터의 경우 어떤 컬럼을 기준으로 분석할지 고민했고, 범죄·교통사고·화재 등급을 기준으로 위험 지역을 필터링하는 분석을 수행했습니다.
  - 실제 생체신호 기반 데이터가 어떻게 구성되어 있는지 확인하고, 혈압(SBP/DBP)과 같은 의료 지표를 시각화하는 과정을 경험해보고 싶었습니다. 이에 PPG 파형을 어떻게 활용할 수 있을지, 시계열 분석과 연결할 수 있는지 고민했습니다.
- 부족한 점
  - 아직은 데이터를 불러오거나 특정 컬럼을 선택하는 과정 등 에서 AI의 도움을 참고하는 경우가 있었습니다. 특히 처음 접하는 데이터 형식에서는 구조를 빠르게 파악하지 못해 시행착오가 있었습니다.
  - 시각화는 가능하지만, 그래프를 통해 얻을 수 있는 인사이트를 깊이 있게 도출하는 능력은 부족하다고 느꼈습니다. 데이터를 단순히 보여주는 수준을 넘어 의미 있는 해석을 수행하기 위해서는 통계적 분석과 도메인 지식이 더 필요하다고 생각했습니다.
- 개선점 및 목표
  - 앞으로는 AI에 의존하기보다 공식 문서를 적극적으로 참고하며 스스로 문제를 해결하고자 합니다. 데이터 구조를 이해하고 전처리 과정을 직접 수행하는 연습을 지속적으로 진행하고자 합니다.
  - 추후 지역안전등급 데이터를 활용하여 지역별 안전등급 예측 모델이나 위험 지역 분류 모델을 만들어보고 싶습니다. 과거 연도별 안전등급 데이터를 수집하여 특정 지역의 미래 안전등급을 예측하는 머신러닝 모델을 설계하는 것이 목표입니다.

