# Generated by Django 5.1.3 on 2024-11-30 05:19

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='부서명')),
                ('description', models.TextField(blank=True, verbose_name='부서 설명')),
            ],
            options={
                'verbose_name': '부서',
                'verbose_name_plural': '부서들',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='직책명')),
                ('level', models.PositiveIntegerField(verbose_name='직책 레벨')),
            ],
            options={
                'verbose_name': '직책',
                'verbose_name_plural': '직책들',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('employee_id', models.CharField(max_length=20, unique=True, verbose_name='사원번호')),
                ('phone_number', models.CharField(blank=True, max_length=15, verbose_name='전화번호')),
                ('join_date', models.DateField(verbose_name='입사일')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='프로필 사진')),
                ('is_active', models.BooleanField(default=True, verbose_name='재직 여부')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedules.department', verbose_name='부서')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedules.position', verbose_name='직책')),
            ],
            options={
                'verbose_name': '직원',
                'verbose_name_plural': '직원들',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='일정 제목')),
                ('description', models.TextField(blank=True, verbose_name='상세 내용')),
                ('start_date', models.DateTimeField(verbose_name='시작 일시')),
                ('end_date', models.DateTimeField(verbose_name='종료 일시')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_schedules', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('participants', models.ManyToManyField(blank=True, related_name='participating_schedules', to=settings.AUTH_USER_MODEL, verbose_name='참여자')),
            ],
            options={
                'verbose_name': '일정',
                'verbose_name_plural': '일정들',
                'ordering': ['-start_date'],
            },
        ),
    ]
