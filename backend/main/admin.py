from django.contrib import admin
from .models import ConsumedFood, DailyLog, NutritionalGoal, Food


# Register your models here.


class ConsumedFoodStacked(admin.StackedInline):
    model = ConsumedFood


class DailyLogAdmin(admin.ModelAdmin):
    inlines = [ConsumedFoodStacked]
    list_display = ["id", "user", "meal", "weight", "is_active", "date", "created_at", "updated_at"]
    list_filter = ["meal", "is_active", "created_at", "updated_at"]


class NutritionalGoalAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "is_active", "date", "created_at", "updated_at"]
    list_filter = ["is_active", "created_at", "updated_at"]


class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "fcd_id", "name", "calories", "protein", "carbs", "fats"]


admin.site.register(DailyLog, DailyLogAdmin)
admin.site.register(NutritionalGoal, NutritionalGoalAdmin)
admin.site.register(Food, FoodAdmin)
