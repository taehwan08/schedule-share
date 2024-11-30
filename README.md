# 일정 공유 시스템

회사 내 직원들의 일정을 관리하고 공유하기 위한 웹 애플리케이션입니다.

## 주요 기능

- 일정 관리 (생성, 수정, 삭제)
- 캘린더 뷰
- 일정 목록 뷰
- 사용자 관리 (관리자 전용)
- 부서 및 직책 관리

## 기술 스택

- Python 3.10+
- Django 5.1.3
- Bootstrap 5.3.0
- FullCalendar 5.11.3

## 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/taehwan08/schedule-share.git
cd schedule-share
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

5. 초기 데이터 설정
```bash
python manage.py setup_initial_data
```

6. 개발 서버 실행
```bash
python manage.py runserver
```

## 초기 관리자 계정

- 아이디: admin
- 비밀번호: admin123!

## 라이선스

MIT License 