from django.contrib import admin
from . import models


@admin.register(models.Sales)
class SalesAdmin(admin.ModelAdmin):

    """Sales Admin Definition"""

    raw_id_fields = (
        "customer_name",
        "ordered_store",
    )


@admin.register(models.InsertCsv_db)
class InsertCsv_dbAdmin(admin.ModelAdmin):

    """InsertCsv_db Admin Definition"""

    list_display = (
        "order_num",
        "order_type",
        "store_name",
        "licence_num",
        "start_address",
        "payment_method",
        "total_amount",
        "order_date",
        "order_time",
    )

    ordering = (
        "order_num",
        "order_type",
        "total_amount",
        "order_date",
    )

    list_filter = ("order_type",)

    search_fields = (
        "order_type",
        "store_name",
    )


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    """PostAdmin Definition"""

    list_display = ("title", "head_image", "file_upload", "created_at", "updated_at")
