# [위클리 챌린지] 2주차

## 📋 과제


1. HTTP 내용 정리
2. FastAPI로 커뮤니티 서비스의 백엔드를 구현해보세요
    1. HTTP REST API 설계 및 구현
    2. AI 모델 서빙
    3. 데이터베이스 적용하기
    4. 구조 개선하기(예: Route - Controller - Model 패턴을 적용)
    5. (선택) HTML/CSS/S나 스트림릿으로 프론트엔드 만들기


## 📢 설명

1. HTTP 내용 정리
    - [TIL (2026-05-18)](https://github.com/100-hours-a-week/KTB4-emjay-AI/blob/main/TIL/week2/2026-05-18.md)

2. FastAPI로 커뮤니티 서비스의 백엔드 구현
    - [x] 게시글 생성, 조회, 수정, 삭제 구현
    - [x] 댓글 작성, 조회, 수정, 삭제 구현
    - [x] AI 모델 서빙: 게시글과 댓글의 내용을 기반으로 전반적인 내용을 분석하는 AI 요약 도우미
    - [x] 데이터베이스 적용 완료
    - [x] router - controller - model 패턴 적용
    - [ ] 스트림릿으로 프론트엔드 만들기

  
| 기능 | 설명 |
|---|---|
| 기능 | 1. 사용자가 게시글을 생성하고, 게시글 목록 및 특정 게시글을 조회 가능<br>2. 특정 게시글에 댓글 작성, 조회, 수정, 삭제 가능<br>3. 특정 게시글의 내용과 해당 글의 댓글을 기반으로 내용 요약 |
| 추가<br>목표 | 1. 스트림릿으로 프론트엔드 만들기<br>2. AI 모델 추가하기 |

## 🚀 사용법

### 1) FastAPI
```bash
# 1. 가상환경 생성 및 활성화
python3 -m venv .venv 
source .venv/bin/activate

# 현재 python 경로 확인
which python3

# 2. FastAPI 및 실행 라이브러리 설치
pip install fastapi[standard] 

# 3. FastAPI 서버 실행
fastapi dev
```

### 2) LLM
```bash
# 1. Ollama 관련 라이브러리 설치
uv add ollama pyyaml

# 2. Ollama 서버 실행
ollama serve

# 3. Gemma4 모델 다운로드
ollama pull gemma4

# 4. 모델 실행 테스트
ollama run gemma4
```

### 3) 전체 실행 순서
```bash
# 1. 터미널 1
ollama serve

# 2. 터미널 2
source .venv/bin/activate
fastapi dev
```


## 💻 실행 예시

### 1) API EndPoint

#### 게시글 (Posts)
| 메소드 | 경로 | 설명 |
|---|---|---|
| GET | `/posts` | 게시글 목록 조회 |
| POST | `/posts` | 게시글 생성 |
| GET | `/posts/{post_id}` | 특정 게시글 조회 |
| DELETE | `/posts/{post_id}` | 게시글 삭제 |
| PATCH | `/posts/{post_id}` | 게시글 수정 |

#### 댓글 (Comments)
| 메소드 | 경로 | 설명 |
|---|---|---|
| POST | `/posts/{post_id}/comments` | 댓글 작성 |
| GET | `/posts/{post_id}/comments` | 특정 게시글의 댓글 목록 조회 |
| PATCH | `/posts/{post_id}/comments/{comment_id}` | 특정 게시글의 댓글 수정 |
| DELETE | `/posts/{post_id}/comments/{comment_id}` | 특정 게시글의 댓글 삭제 |

#### AI 요약 (Summary)
| 메소드 | 경로 | 설명 |
|---|---|---|
| POST | `/posts/{post_id}/summary` | 게시글 및 댓글 종합 요약 |

### 2) Swagger
[Swagger](http://127.0.0.1:8000/docs)

<img width="1455" height="854" alt="fastapi docs" src="https://github.com/user-attachments/assets/d62e5467-2372-47c6-8c75-5ccee03551f1" />


### 3) AI summary
#### post
```text
{
  "id": 4,
  "title": "위클리 챌린지",
  "content": "이번주 위클리 챌린지 과제는 커뮤니티 서비스 만들기. 게시글 및 댓글의 작성, 조회, 수정, 삭제 기능 구현 완료",
  "author": "emjay",
  "comment_count": 5,
  "view_count": 1,
  "created_at": "2026-05-23T16:38:24"
}
```

#### comments
```text
[
  {
    "id": 7,
    "post_id": 4,
    "content": "AI 모델 서빙 테스트",
    "author": "emjay",
    "created_at": "2026-05-23T16:40:12"
  },
  {
    "id": 6,
    "post_id": 4,
    "content": "구조 개선: router - controller - model 패턴 적용",
    "author": "emjay",
    "created_at": "2026-05-23T16:40:03"
  },
  {
    "id": 5,
    "post_id": 4,
    "content": "데이터베이스 적용",
    "author": "emjay",
    "created_at": "2026-05-23T16:39:39"
  },
  {
    "id": 4,
    "post_id": 4,
    "content": "댓글 작성, 조회, 수정, 삭제 구현",
    "author": "emjay",
    "created_at": "2026-05-23T16:39:30"
  },
  {
    "id": 3,
    "post_id": 4,
    "content": "게시글 작성, 조회, 수정, 삭제 구현",
    "author": "emjay",
    "created_at": "2026-05-23T16:39:19"
  }
]
```

#### result
<img width="1397" height="312" alt="summary result" src="https://github.com/user-attachments/assets/9e71ecef-99d4-4ae3-b0b4-c0f7626b88d2" />


## 📁 파일 구조

```text
02/
├── controller/
│   ├── __init__.py
│   ├── comment.py
│   ├── post.py
│   └── summary.py
│
├── model/
│   ├── __init__.py
│   ├── comment.py
│   └── post.py
│
├── router/
│   ├── __init__.py
│   ├── comment.py
│   ├── default.py
│   ├── post.py
│   └── summary.py
│
├── schemas/
│   ├── __init__.py
│   ├── comment.py
│   ├── post.py
│   └── summary.py
│
├── .gitignore
├── .python-version
├── database.py
├── main.py
├── prompts.yaml
├── pyproject.toml
└── uv.lock
```

## 📝 회고
이번 과제를 진행하며 FastAPI 기반 REST API 서버와 AI 모델 서빙 구조를 직접 구현해볼 수 있었습니다. FastAPI에서 실제 API 서버를 어떻게 설계하고 기능별로 구조화해야 하는지 익숙하지 않았기 때문에, 특히 `router-controller-model` 구조로 역할을 분리하는 과정에 많은 시간을 썼던 것 같습니다. 이번 과제를 통해 API를 구현하면서 유지보수를 고려한 프로젝트 구조 설계와 AI 모델 서빙 흐름까지 경험했습니다.

- `router-controller-model` 구조화
    - router에서는 URL과 API 엔드포인트를 관리하고, controller에서는 실제 비즈니스 로직을 수행하며, model에는 데이터베이스 구조를 정의, schema는 요청 및 응답 데이터를 검증하도록 했습니다. 이를 통해 게시글 + 댓글 + AI 요약 등 기능이 추가되더라도 유지보수가 쉽도록 구조화하는 필요성을 체감했습니다.
- router 구조 관리
    - FastAPI의 Swagger Docs에서는 router 단위로 API가 그룹화되기 때문에, 각 기능별로 router를 명확히 나누는 것이 유지보수와 추후 협업 측면에서 중요함을 체감했습니다. 단순히 기능 분리 목적 뿐만 아니라, 다른 개발자와 협업하거나 API 문서를 확인할 때 각 router가 어떤 역할 단위를 수행하는지 직관적으로 이해할 수 있도록 했습니다.
- `gemma4` 선택
    - 이번 과제에서는 Ollama 기반 LLM을 활용해 게시글 + 댓글 종합 요약 기능을 구현했습니다. 이때 모델은 gemma4를 선택했습니다. 그 이유는 비교적 가벼운 크기 대비 응답 속도가 빠르고, 로컬 환경에서도 부담 없이 실행할 수 있다고 생각했습니다.
    - FastAPI 서버에서 Ollama를 호출해 게시글과 댓글 데이터를 prompt에 함께 전달하고, 이를 기반으로 '글의 주제 + 댓글의 주요 의견 - 종합 요약'을 생성하는 구조를 구현했습니다.
