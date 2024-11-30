from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department, Position, Schedule


class CustomUserAdmin(UserAdmin):
    list_display = (
        "employee_id",
        "username",
        "email",
        "first_name",
        "last_name",
        "department",
        "position",
        "is_active",
    )
    list_filter = ("is_active", "department", "position")
    fieldsets = UserAdmin.fieldsets + (
        (
            "직원 정보",
            {
                "fields": (
                    "employee_id",
                    "department",
                    "position",
                    "phone_number",
                    "join_date",
                    "profile_image",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "직원 정보",
            {
                "fields": (
                    "employee_id",
                    "department",
                    "position",
                    "phone_number",
                    "join_date",
                    "profile_image",
                )
            },
        ),
    )
    search_fields = ("username", "first_name", "last_name", "employee_id", "email")
    ordering = ("employee_id",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Schedule)
