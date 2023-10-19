# 설치 파일 다운
```py
pip freeze > requirements.txt
```
# 실행
```py
python manage.py runserver
```
# testcode 실행
```py
pytest
```
### companies 실행
```py
pytest companies/tests.py
```
### recruits 실행
```py
pytest recruits/tests.py
```
### users 실행
```py
pytest users/tests.py
```
---
## 1. Company 등록
http://127.0.0.1:8000/api/company/new/

```py
{
    "company_name":"다음",
    "address":"서울시 강남구 서초동",
    "country":"대한민국",햣
    "city":"서울"
}
```
결과값 <br>
```py
{
    "id": 6,
    "company_name": "다음",
    "address": "서울시 강남구 서초동",
    "country": "대한민국",
    "city": "서울"
}
```
## 1-1. company list 조회 
http://127.0.0.1:8000/api/company/new/

```py
[
    {
        "id": 1,
        "company_name": "원티드",
        "address": "서울시 송파구 신천동",
        "country": "대한민국",
        "city": "서울"
    },
    {
        "id": 2,
        "company_name": "원티드랩",
        "address": "서울시 송파구 잠실동",
        "country": "대한민국",
        "city": "잠실"
    },
    {
        "id": 3,
        "company_name": "네이버",
        "address": "경기도 성남시 분당구",
        "country": "대한민국",
        "city": "분당"
    },
    {
        "id": 4,
        "company_name": "토스",
        "address": "서울시 강남구 서초동",
        "country": "한국",
        "city": "강남"
    },
    {
        "id": 5,
        "company_name": "토스페이먼츠",
        "address": "서울시 성동구",
        "country": "대한민국",
        "city": "서울"
    },
    {
        "id": 6,
        "company_name": "다음",
        "address": "서울시 강남구 서초동",
        "country": "대한민국",
        "city": "서울"
    }
]
```
## 1-2. company 조회, 수정 및 삭제
http://127.0.0.1:8000/api/company/list/3/

**GET**
```py
HTTP 200 OK
{
    "id": 3,
    "company_name": "네이버",
    "address": "경기도 성남시 분당구",
    "country": "대한민국",
    "city": "분당"
}
```
**PUT**
```py
{
    "city": "성남"
}
```
결과값
```py
HTTP 200 OK
{
    "id": 3,
    "company_name": "네이버",
    "address": "경기도 성남시 분당구",
    "country": "대한민국",
    "city": "성남" # 수정됨
}
```
**DELETE**
```py
HTTP 204 No Content
{
    "detail": "찾을 수 없습니다."
}
```
---
## 2. Recruit 등록
```py
{
    "company":"원티드",
    "title":"풀스택 개발자 채용",
    "position":"풀스택",
    "reward":"300000",
    "skill":"python, java, javascript",
    "content":"풀스택 개발자 뽑아요"
}
```
결과값
```py
HTTP 201 Created
{
    "id": 6,
    "company": "원티드",
    "title": "풀스택 개발자 채용",
    "position": "풀스택",
    "reward": 300000,
    "skill": "python, java, javascript",
    "content": "풀스택 개발자 뽑아요"
}
```
**회사가 등록되어있지 않은 경우**
```py
HTTP 400 Bad Request
{
    "message": "회사를 찾을 수 없습니다."
}
```

## 2-1. Recruit 리스트 조회 (페이지네이션 적용)
http://127.0.0.1:8000/api/recruits/list/

```py
HTTP 200 OK
{
    "count": 6,
    "next": "http://127.0.0.1:8000/api/recruits/list/?page=2",
    "previous": null,
    "results": [
        {
            "id": 7,
            "company": "원티드",
            "country": "대한민국",
            "city": "서울",
            "title": "머신러닝 개발자 채용",
            "position": "백엔드",
            "reward": 300000,
            "skill": "Python",
            "content": "머신러닝 개발자 채용합니다"
        },
        {
            "id": 6,
            "company": "원티드",
            "country": "대한민국",
            "city": "서울",
            "title": "풀스택 개발자 채용",
            "position": "풀스택",
            "reward": 300000,
            "skill": "python, java, javascript",
            "content": "풀스택 개발자 뽑아요"
        },
        {
            "id": 5,
            "company": "원티드",
            "country": "대한민국",
            "city": "서울",
            "title": "프론트엔드 개발자 채용",
            "position": "프론트",
            "reward": 200000,
            "skill": "javascript",
            "content": "react, next 자유롭게 사용 가능 하신 분"
        },
        {
            "id": 3,
            "company": "토스",
            "country": "한국",
            "city": "강남",
            "title": "토스 개발자 채용",
            "position": "풀스택",
            "reward": 200000,
            "skill": "직군 별 상이",
            "content": "자세한 내용은 홈페이지를 참조해주세요."
        },
        {
            "id": 2,
            "company": "원티드랩",
            "country": "대한민국",
            "city": "잠실",
            "title": "백엔드 채용",
            "position": "백엔드",
            "reward": 200000,
            "skill": "python,django",
            "content": "백엔드 개발자 뽑아요"
        }
    ]
}
```
## 2-2 Recruit 검색
**company,title,position,reward,skill,content 내의 단어 모두 검색 가능 / 대소문자 상관없음**

http://127.0.0.1:8000/api/recruits/list/?search=python
```py
HTTP 200 OK
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 7,
            "company": "원티드",
            "country": "대한민국",
            "city": "서울",
            "title": "머신러닝 개발자 채용",
            "position": "백엔드",
            "reward": 300000,
            "skill": "Python",
            "content": "머신러닝 개발자 채용합니다"
        },
        {
            "id": 6,
            "company": "원티드",
            "country": "대한민국",
            "city": "서울",
            "title": "풀스택 개발자 채용",
            "position": "풀스택",
            "reward": 300000,
            "skill": "python, java, javascript",
            "content": "풀스택 개발자 뽑아요"
        },
        {
            "id": 2,
            "company": "원티드랩",
            "country": "대한민국",
            "city": "잠실",
            "title": "백엔드 채용",
            "position": "백엔드",
            "reward": 200000,
            "skill": "python,django",
            "content": "백엔드 개발자 뽑아요"
        },
        {
            "id": 1,
            "company": "원티드",
            "country": "대한민국",
            "city": "서울",
            "title": "개발자뽑아요",
            "position": "백엔드",
            "reward": 200000,
            "skill": "python",
            "content": "파이썬 개발자 뽑아요"
        }
    ]
}
```
## 2-3 Recruit 조회, 수정 및 삭제 
**same_company_recruits 에 같은 회사의 다른 공고 나열** <br>
http://127.0.0.1:8000/api/recruits/list/1/

**GET**
```py
HTTP 200 OK
{
    "id": 1,
    "company": "원티드",
    "title": "개발자뽑아요",
    "position": "백엔드",
    "reward": 200000,
    "skill": "python",
    "content": "파이썬 개발자 뽑아요",
    "same_company_recruits": [
        {
            "id": 5,
            "title": "프론트엔드 개발자 채용"
        },
        {
            "id": 6,
            "title": "풀스택 개발자 채용"
        },
        {
            "id": 7,
            "title": "머신러닝 개발자 채용"
        }
    ]
}
```
**PUT**
```py
{
    "title": "백엔드 개발자 채용",
    "skill":"java,spring",
    "content": "언어 이해도가 높으신 분 우대"
}
```
결과값
```py
HTTP 200 OK
{
    "id": 1,
    "company": "원티드",
    "title": "백엔드 개발자 채용", # 수정됨
    "position": "백엔드",
    "reward": 200000,
    "skill": "java,spring", # 수정됨
    "content": "언어 이해도가 높으신 분 우대" # 수정됨
}
```
**채용공고에서는 회사명 변경 불가**
```py
HTTP 400 Bad Request
{
    "message": "회사는 수정할 수 없습니다."
}
```
**DELETE**
```py
HTTP 204 No Content
{
    "message": "삭제되었습니다."
}
```
---
## 3. User 등록
http://127.0.0.1:8000/api/users/new/

```py
{"username":"gogo","password":"qpqp1010"}
```
결과값
```py
HTTP 201 Created
{
    "id": 10,
    "username": "gogo",
    "password": "pbkdf2_sha256$600000$zAtxxOmZ6nywsSdCs6VvDG$ow7Rv6phhtty15C97IGDNNLySQwvcx4bUJle7SpZIoU=",
    "user_recruit": null
}
```
## 3-1. User 채용 공고 지원
```py
{"recruit_id":"5"}
```
결과값
```py
HTTP 200 OK
{
    "id": 6,
    "username": "eeoo",
    "password": "!H36qhsmjeJpQdNDf3ZQZ3Gv3tVfZ58r96L1thh8U",
    "user_recruit": {
        "recruit_id": 5,
        "company": "원티드",
        "title": "프론트엔드 개발자 채용"
    }
}
```
이미 지원한 공고가 있는 경우
```py
HTTP 400 Bad Request
{
    "message": "이미 지원한 채용공고가 있습니다."
}
```
