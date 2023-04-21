from django.urls import path
from . import models, views

app_name = "events"

urlpatterns = [
    path("", views.EventLV.as_view(), name="index"),
    path("events", views.EventLV.as_view(), name="events_list"),
    path("events/<int:pk>", views.EventDV.as_view(), name="event_detail"),
    path("images/<int:pk>", views.ImageDV.as_view(), name="image_detail"),
]
