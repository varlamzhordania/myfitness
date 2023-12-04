from django import forms
from django.forms import inlineformset_factory
from .models import DailyLog, MEAL_CHOICES, ConsumedFood, Food
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"


class ConsumedFoodForm(forms.ModelForm):
    class Meta:
        model = ConsumedFood
        fields = ['food', 'quantity']
        widgets = {
            'food': forms.TextInput(attrs={'class': 'form-control autocomplete', "id": "auto-complete-food"}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DailyLogCreationForm(forms.ModelForm):
    meal = forms.ChoiceField(
        required=True, label=_("Meal"), choices=MEAL_CHOICES, widget=forms.Select(
            attrs={
                "class": "form-select",
                "id": "meal",
            }
        )
    )
    weight = forms.FloatField(
        initial=1,
        step_size=0.001,
        required=True, label=_("Weight(Kg)"), min_value=1, widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    date = forms.DateField(
        required=True, initial=datetime.today().date(), widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date"
            }
        )
    )

    class Meta:
        model = DailyLog
        fields = ["meal", "weight", "date"]


ConsumedFoodFormSet = inlineformset_factory(DailyLog, ConsumedFood, form=ConsumedFoodForm, extra=1)
