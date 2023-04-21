from django.urls import path
from key_statistics import views as key_statistics_views

app_name = "core"

urlpatterns = [
    path("", key_statistics_views.DashBoardView.as_view(), name="home"),
]
