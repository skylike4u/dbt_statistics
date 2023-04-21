from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class EventLV(ListView):

    """EventLV Definition"""

    model = models.Event_info
    context_object_name = "events"
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = models.Event_info.objects.get(pk=1)
        context["photos"] = event.event_info.all()
        return context


class EventDV(DetailView):

    "Events Detail Definition"

    model = models.Event_info


class ImageDV(DetailView):

    """Image(Photo) Detail Definition"""

    model = models.Event_image
