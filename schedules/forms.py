from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Schedule, CustomUser


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ["title", "description", "start_date", "end_date", "participants"]
        widgets = {
            "start_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("종료 일시는 시작 일시보다 늦어야 합니다.")


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "employee_id",
            "email",
            "first_name",
            "last_name",
            "department",
            "position",
            "phone_number",
            "join_date",
        )
        widgets = {
            "join_date": forms.DateInput(attrs={"type": "date"}),
        }


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "employee_id",
            "email",
            "first_name",
            "last_name",
            "department",
            "position",
            "phone_number",
            "join_date",
            "is_active",
        )
        widgets = {
            "join_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.is_staff:
            self.fields["is_active"].disabled = True
            self.fields["is_active"].help_text = (
                "관리자 계정의 상태는 변경할 수 없습니다."
            )
