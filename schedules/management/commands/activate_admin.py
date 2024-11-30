from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "관리자 계정을 활성화합니다."

    def handle(self, *args, **kwargs):
        User = get_user_model()
        admin = User.objects.get(username="admin")
        admin.is_active = True
        admin.save()
        self.stdout.write(self.style.SUCCESS("관리자 계정이 활성화되었습니다."))
