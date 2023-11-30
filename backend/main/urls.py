from django.urls import path
from .views import home, dashboard, logs

app_name = "main"

urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logs/', logs, name="logs"),
]
