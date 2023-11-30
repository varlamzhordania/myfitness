from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import DailyLog, NutritionalGoal
from datetime import datetime, timedelta


# Create your views here.


def home(request, *args, **kwargs):
    my_context = {
        "Title": "Home"
    }
    return render(request, "home.html", my_context)


@login_required
def dashboard(request, *args, **kwargs):
    today = datetime.today()
    thirty_days_ago = today - timedelta(days=30)
    percentage_calories = 0
    percentage_protein = 0
    percentage_carbs = 0
    percentage_fats = 0
    days_remaining = 0
    # Fetch the user's nutritional goal based on the date it was created
    nutritional_goal = NutritionalGoal.objects.filter(user=request.user, is_active=True).first()

    # Fetch the user's daily logs up to today
    daily_logs = DailyLog.objects.filter(user=request.user, date__lte=today)

    today_logs = daily_logs.filter(date=today)

    thirty_days_logs_ago = daily_logs.filter(date__gte=thirty_days_ago).order_by("date")

    # Calculate the total consumed values from all daily logs
    if nutritional_goal:
        total_calories_consumed = sum(log.total_calories_consumed() for log in daily_logs)
        total_protein_consumed = sum(log.total_protein_consumed() for log in daily_logs)
        total_carbs_consumed = sum(log.total_carbs_consumed() for log in daily_logs)
        total_fats_consumed = sum(log.total_fats_consumed() for log in daily_logs)

        # Calculate the percentage of goal achieved
        percentage_calories = (total_calories_consumed / nutritional_goal.calorie_goal) * 100
        percentage_protein = (total_protein_consumed / nutritional_goal.protein_goal) * 100
        percentage_carbs = (total_carbs_consumed / nutritional_goal.carbs_goal) * 100
        percentage_fats = (total_fats_consumed / nutritional_goal.fats_goal) * 100

        days_remaining = nutritional_goal.date - nutritional_goal.created_at.date()

    my_context = {
        "Title": "dashboard",
        "logs": today_logs,
        "goal": nutritional_goal,
        "thirty_days_logs_ago": thirty_days_logs_ago,
        "days_goal_remaining": days_remaining.days,
        "percentage_calories": round(percentage_calories, 2),
        "percentage_protein": round(percentage_protein, 2),
        "percentage_carbs": round(percentage_carbs, 2),
        "percentage_fats": round(percentage_fats, 2),
    }
    return render(request, "dashboard.html", my_context)


@login_required
def logs(request, *args, **kwargs):
    page = request.GET.get("page", 0)

    queryset = DailyLog.objects.filter(user=request.user)

    pagination = Paginator(queryset, per_page=10)
    item = pagination.get_page(page)

    my_context = {
        "Title": "Logs List",
        "logs": item,
    }
    return render(request, "logs.html", my_context)
