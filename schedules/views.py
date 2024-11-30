from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from .models import Schedule, CustomUser
from .forms import ScheduleForm, CustomUserCreationForm, CustomUserChangeForm
from datetime import datetime


def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def user_list(request):
    users = CustomUser.objects.all().order_by("employee_id")
    return render(request, "schedules/user_list.html", {"users": users})


@user_passes_test(is_admin)
def user_create(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "사용자가 생성되었습니다.")
            return redirect("schedules:user_list")
    else:
        form = CustomUserCreationForm()
    return render(
        request, "schedules/user_form.html", {"form": form, "title": "사용자 생성"}
    )


@user_passes_test(is_admin)
def user_edit(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "사용자 정보가 수정되었습니다.")
            return redirect("schedules:user_list")
    else:
        form = CustomUserChangeForm(instance=user)
    return render(
        request, "schedules/user_form.html", {"form": form, "title": "사용자 수정"}
    )


@user_passes_test(is_admin)
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if user.is_staff:
        messages.error(request, "관리자 계정은 삭제할 수 없습니다.")
        return redirect("schedules:user_list")

    if request.method == "POST":
        user.is_active = False
        user.save()
        messages.success(request, "사용자가 비활성화되었습니다.")
        return redirect("schedules:user_list")
    return render(request, "schedules/user_confirm_delete.html", {"user": user})


@login_required
def schedule_list(request):
    schedules = Schedule.objects.filter(
        participants=request.user
    ) | Schedule.objects.filter(created_by=request.user)
    return render(request, "schedules/schedule_list.html", {"schedules": schedules})


@login_required
def schedule_calendar(request):
    return render(request, "schedules/schedule_calendar.html")


@login_required
def schedule_create(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.created_by = request.user
            schedule.save()
            form.save_m2m()  # 다대다 관계 저장
            messages.success(request, "일정이 생성되었습니다.")
            return redirect("schedules:schedule_list")
    else:
        form = ScheduleForm()
    return render(
        request, "schedules/schedule_form.html", {"form": form, "title": "일정 생성"}
    )


@login_required
def schedule_edit(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == "POST":
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, "일정이 수정되었습니다.")
            return redirect("schedules:schedule_list")
    else:
        form = ScheduleForm(instance=schedule)
    return render(
        request, "schedules/schedule_form.html", {"form": form, "title": "일정 수정"}
    )


@login_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == "POST":
        schedule.delete()
        messages.success(request, "일정이 삭제되었습니다.")
        return redirect("schedules:schedule_list")
    return render(
        request, "schedules/schedule_confirm_delete.html", {"schedule": schedule}
    )


@login_required
def schedule_api(request):
    start = request.GET.get("start")
    end = request.GET.get("end")

    schedules = Schedule.objects.filter(
        participants=request.user
    ) | Schedule.objects.filter(created_by=request.user)

    if start and end:
        start_date = datetime.fromisoformat(start.replace("Z", "+00:00"))
        end_date = datetime.fromisoformat(end.replace("Z", "+00:00"))
        schedules = schedules.filter(start_date__gte=start_date, end_date__lte=end_date)

    events = []
    for schedule in schedules:
        events.append(
            {
                "id": schedule.id,
                "title": schedule.title,
                "start": schedule.start_date.isoformat(),
                "end": schedule.end_date.isoformat(),
                "url": f"/schedules/{schedule.id}/edit/",
            }
        )

    return JsonResponse(events, safe=False)
