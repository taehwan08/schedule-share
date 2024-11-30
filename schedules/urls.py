from django.urls import path
from . import views

app_name = "schedules"

urlpatterns = [
    path("", views.schedule_list, name="schedule_list"),
    path("calendar/", views.schedule_calendar, name="schedule_calendar"),
    path("create/", views.schedule_create, name="schedule_create"),
    path("<int:pk>/edit/", views.schedule_edit, name="schedule_edit"),
    path("<int:pk>/delete/", views.schedule_delete, name="schedule_delete"),
    path("api/events/", views.schedule_api, name="schedule_api"),
    # 사용자 관리 URL
    path("users/", views.user_list, name="user_list"),
    path("users/create/", views.user_create, name="user_create"),
    path("users/<int:pk>/edit/", views.user_edit, name="user_edit"),
    path("users/<int:pk>/delete/", views.user_delete, name="user_delete"),
]
