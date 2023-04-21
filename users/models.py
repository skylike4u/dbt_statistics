from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    """Custom User Model definition"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "others"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Others"),
    )

    # GENDER_MALE가 데이터베이스로 갈거고, "Male"이 admin 패널 form에서 보여질 값임.

    person_name = models.CharField(max_length=10, blank=True)
    company_name = models.CharField(max_length=15, blank=True, null=True)
    company_department = models.CharField(max_length=15, null=True, blank=True)
    company_position = models.CharField(max_length=15, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    # office_tel
    # mobile_phone
    photo = models.ImageField(upload_to="photos", blank=True)
    super_host = models.BooleanField(default=False)
    user_info = models.TextField(default="")
