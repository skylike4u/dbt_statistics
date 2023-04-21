from django.urls import path
from . import views


app_name = "key_statistics"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dashboard/", views.DashBoardView.as_view(), name="dashboard"),
    path("<int:pk>/", views.SalesDetail.as_view(), name="SalesDetail"),
    path("post_list", views.PostView.as_view(), name="post_list"),
    path("post/<int:pk>", views.PostViewDetail.as_view(), name="post_detail"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("question_list/", views.Question, name="question_list"),
    path("answear/create/<int:pk>", views.AnswearCreate, name="AnswearCreate"),
    path("question_edit/<int:pk>/", views.Question_edit, name="question_edit"),
]
