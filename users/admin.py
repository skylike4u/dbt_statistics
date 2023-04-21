from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# admin.site.register(models.User, CustomUserAdmin)


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom UserAdmin definition"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {"fields": ("person_name", "company_name", "company_department", "photo")},
        ),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": ("gender", "super_host"),
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("super_host",)

    list_display = (
        "person_name",
        "company_name",
        "company_department",
        "company_position",
        "photo",
        "super_host",
        "user_info",
    )
