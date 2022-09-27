# 레포지토리 명
## TTS-preprocess-backend

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [프로젝트 기술 스택](#프로젝트-기술-스택)
3. [개발 기간](#개발-기간)
4. [개발 인원](#개발-인원)
5. [API 목록](#API-목록)


<br>


## 프로젝트 개요
- TTS 딥러닝 모델에 사용하기 위한 데이터 전처리 백엔드 구현
- user 기능 추가
- Project 기능 추가
- Project 단위로 n개의 Audio 추가


<br>

## 과제 요구사항 분석
### 1. 요구사항
- 요구사항

<br>

## 프로젝트 기술 스택

### Backend
<section>
<img src="https://img.shields.io/badge/Django-092E20?logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django%20REST%20Framework-092E20?logo=Django&logoColor=white"/>
</section>

### DB
<section>
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=MySQL&logoColor=white"/>
</section>

### Tools
<section>
<img src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white"/>
<img src="https://img.shields.io/badge/Discord-5865F2?logo=Discord&logoColor=white">
<img src="https://img.shields.io/badge/Postman-FF6C37?logo=Postman&logoColor=white">
</section>


<br>


## 개발 기간
- 2022/09/22~2022/09/27


<br>


## 개발 인원
| 김현수 |
| ------ |
| [Github](https://github.com/HyeonsooKim) |


<br>


## ERD
<img width="813" alt="스크린샷 2022-09-27 오후 11 21 22" src="https://user-images.githubusercontent.com/48047773/192552501-b3686520-849a-45c4-b4bc-ffd1d05b62b8.png">


<br>


## API 목록
![127 0 0 1_8000_api_v1_swagger (1)](https://user-images.githubusercontent.com/48047773/192550332-418d9600-ef7d-4295-a968-6f71880698ad.png)


<br>


## 프로젝트 시작 방법
1. 로컬에서 실행할 경우
```bash
# 프로젝트 clone(로컬로 내려받기)
git clone -b develop --single-branch ${github 주소}
cd ${디렉터리 명}

# 가상환경 설정
python -m venv ${가상환경명}
source ${가상환경명}/bin/activate
# window (2 ways) 
# 1> ${가상환경명}/Scripts/activate
# 2> activate

# 라이브러리 설치
pip install -r requirements.txt
# 실행
python manage.py runserver
```

<br>
