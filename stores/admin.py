from django.contrib import admin
from . import models


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):

    """Store Admin Definition"""

    # fieldsets = ()

    list_display = (
        "store_name",
        "store_license_num",
        "dbt_category",
        "business_type",
        "store_adress",
        "menu",
    )

    list_filter = (
        "store_name",
        "dbt_category",
    )

    ordering = (
        "store_name",
        "dbt_category",
    )

    search_fields = (
        "store_name",
        "dbt_category",
    )
