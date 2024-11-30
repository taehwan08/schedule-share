from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name="부서명")
    description = models.TextField(blank=True, verbose_name="부서 설명")

    class Meta:
        verbose_name = "부서"
        verbose_name_plural = "부서들"

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name="직책명")
    level = models.PositiveIntegerField(verbose_name="직책 레벨")

    class Meta:
        verbose_name = "직책"
        verbose_name_plural = "직책들"

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    employee_id = models.CharField(max_length=20, unique=True, verbose_name="사원번호")
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, verbose_name="부서"
    )
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, verbose_name="직책"
    )
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="전화번호")
    join_date = models.DateField(verbose_name="입사일")
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True, verbose_name="프로필 사진"
    )
    is_active = models.BooleanField(default=True, verbose_name="재직 여부")

    class Meta:
        verbose_name = "직원"
        verbose_name_plural = "직원들"

    def __str__(self):
        return f"{self.employee_id} - {self.get_full_name()}"


class Schedule(models.Model):
    title = models.CharField(max_length=200, verbose_name="일정 제목")
    description = models.TextField(blank=True, verbose_name="상세 내용")
    start_date = models.DateTimeField(verbose_name="시작 일시")
    end_date = models.DateTimeField(verbose_name="종료 일시")
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="created_schedules",
        verbose_name="작성자",
    )
    participants = models.ManyToManyField(
        CustomUser,
        related_name="participating_schedules",
        blank=True,
        verbose_name="참여자",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")

    class Meta:
        ordering = ["-start_date"]
        verbose_name = "일정"
        verbose_name_plural = "일정들"

    def __str__(self):
        return self.title
