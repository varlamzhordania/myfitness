from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

MEAL_CHOICES = [
    ('breakfast', _('Breakfast')),
    ('lunch', _('Lunch')),
    ('dinner', _('Dinner')),
    ('snack', _('Snack')),
]


class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.FloatField(verbose_name=_("Calories"))
    protein = models.FloatField(verbose_name=_("Protein"))
    carbs = models.FloatField(verbose_name=_("Carbohydrates"))
    fats = models.FloatField(verbose_name=_("Fat"))

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class DailyLog(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_("User"), on_delete=models.CASCADE)
    meal = models.CharField(
        max_length=20,
        choices=MEAL_CHOICES,
        verbose_name=_("Meal"),
        help_text=_("Unique together with Date")
    )
    foods_consumed = models.ManyToManyField(Food, through='ConsumedFood', verbose_name=_("Foods Consumed"))
    weight = models.FloatField(verbose_name=_("Weight"))
    is_active = models.BooleanField(verbose_name=_("Active"), default=True)
    date = models.DateField(verbose_name=_("Date"), help_text=_("Date log belongs to"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date Modified"))

    class Meta:
        ordering = ['-id']
        unique_together = ['date', 'meal', 'user']

    def __str__(self):
        return f"{self.user.username}'s Log - {self.date} - {self.get_meal_display()}"

    def total_calories_consumed(self):
        return sum(cf.total_calories() for cf in self.consumedfood_set.all())

    def total_protein_consumed(self):
        return sum(cf.total_protein() for cf in self.consumedfood_set.all())

    def total_carbs_consumed(self):
        return sum(cf.total_carbs() for cf in self.consumedfood_set.all())

    def total_fats_consumed(self):
        return sum(cf.total_fats() for cf in self.consumedfood_set.all())


class NutritionalGoal(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    calorie_goal = models.FloatField(verbose_name=_("Calorie Goal"))
    protein_goal = models.FloatField(verbose_name=_("Protein Goal"))
    carbs_goal = models.FloatField(verbose_name=_("Carbs Goal"))
    fats_goal = models.FloatField(verbose_name=_("Fats Goal"))
    is_active = models.BooleanField(verbose_name=_("Active"), default=True)
    date = models.DateField(verbose_name=_("Date to Reach Goal"), help_text=_("Date to Reach Goal"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date Modified"))

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.user.username}'s Goals"


class ConsumedFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    daily_log = models.ForeignKey(DailyLog, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), default=1)

    def __str__(self):
        return f"{self.quantity} {self.food.name} in {self.daily_log}"

    def total_calories(self):
        return self.food.calories * self.quantity

    def total_protein(self):
        return self.food.protein * self.quantity

    def total_carbs(self):
        return self.food.carbs * self.quantity

    def total_fats(self):
        return self.food.fats * self.quantity
