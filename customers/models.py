from django.db import models
from core import models as core_models


class Customer(core_models.TimeStampedModel):
    """Customer definition"""

    customer_name = models.CharField(max_length=20, default="")
    customer_adress = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f"{self.customer_name}"
