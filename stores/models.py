from django.db import models
from core import models as core_models


class Store(core_models.TimeStampedModel):
    """Store definition"""

    FOOD_DELIVERY = "food_delivery"
    TRADITIONAL_MARKET = "traditional_market"
    SHOPPING_MALL = "shopping_mall"

    CATEGORY_CHOICES = (
        (FOOD_DELIVERY, "음식배달"),
        (TRADITIONAL_MARKET, "전통시장"),
        (SHOPPING_MALL, "쇼핑몰"),
    )

    store_name = models.CharField(max_length=50, null=False)
    store_license_num = models.CharField(max_length=20, blank=True)
    dbt_category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, blank=True)
    business_type = models.CharField(max_length=50, blank=True)
    # district =
    store_adress = models.CharField(max_length=80, blank=True)
    # store_adress_detail = models.CharField(max_length=80, blank=True)
    store_image = models.ImageField(upload_to="store_images", null=True, blank=True)
    menu = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"[{self.pk}] {self.store_name}"
