from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from schedules.models import Department, Position
from datetime import date


class Command(BaseCommand):
    help = "초기 데이터를 설정합니다."

    def handle(self, *args, **kwargs):
        # 부서 생성
        departments = [
            {"name": "경영지원팀", "description": "인사, 총무, 회계 등 관리 업무"},
            {"name": "개발팀", "description": "소프트웨어 개발 및 유지보수"},
            {"name": "영업팀", "description": "영업 및 고객 관리"},
            {"name": "마케팅팀", "description": "마케팅 전략 수립 및 실행"},
        ]

        for dept_data in departments:
            Department.objects.get_or_create(
                name=dept_data["name"],
                defaults={"description": dept_data["description"]},
            )
        self.stdout.write(self.style.SUCCESS("부서 생성 완료"))

        # 직책 생성
        positions = [
            {"name": "사원", "level": 1},
            {"name": "대리", "level": 2},
            {"name": "과장", "level": 3},
            {"name": "차장", "level": 4},
            {"name": "부장", "level": 5},
            {"name": "이사", "level": 6},
            {"name": "대표이사", "level": 7},
        ]

        for pos_data in positions:
            Position.objects.get_or_create(
                name=pos_data["name"], defaults={"level": pos_data["level"]}
            )
        self.stdout.write(self.style.SUCCESS("직책 생성 완료"))

        # 관리자 계정 생성
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123!",
                employee_id="A0001",
                first_name="관리자",
                last_name="시스템",
                department=Department.objects.get(name="경영지원팀"),
                position=Position.objects.get(name="대표이사"),
                phone_number="010-1234-5678",
                join_date=date.today(),
            )
            self.stdout.write(self.style.SUCCESS("관리자 계정 생성 완료"))
