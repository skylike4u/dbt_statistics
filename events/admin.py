from django.contrib import admin
from . import models

# Register your models here.


class PhotoInline(admin.TabularInline):

    model = models.Event_image


@admin.register(models.Event_info)
class EventinfoAdmin(admin.ModelAdmin):
    """event Info Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "event_name",
                    "event_description",
                    "event_start_date",
                    "event_end_date",
                )
            },
        ),
        ("Event Result", {"fields": ("event_result",)}),
    )

    list_display = ("event_name", "event_description", "event_start_date")

    search_fields = ()


@admin.register(models.Event_image)
class EventimageAdmin(admin.ModelAdmin):

    """Event Image(Photo) Definition"""

    list_display = (
        "image_title",
        "image_description",
        "upload_dt",
    )
