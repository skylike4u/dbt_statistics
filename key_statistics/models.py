from django.db import models
from django.urls import reverse
from django_pandas.managers import DataFrameManager
import os
from core import models as core_models
from stores import models as store_models
from customers import models as customer_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item definition"""

    name = models.CharField(max_length=8)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Sales(AbstractItem):
    """Sales definition"""

    # order_category = models.CharField(max_length=30, null=True)  # 선택으로 만들것
    # payment_option = models.CharField(max_length=30)  # 선택으로 만들것
    order_amount = models.IntegerField(null=True)
    # 가게 주소랑 세부주소 foreign key로 땡겨서 넣을것
    customer_name = models.ForeignKey(
        "customers.Customer", on_delete=models.SET_NULL, null=True
    )
    ordered_store = models.ForeignKey(
        store_models.Store, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name_plural = "sales"

    def __str__(self):
        return f"[{self.ordered_store.dbt_category}] {self.ordered_store} :: {self.order_amount}"
        # 장고가 foreign key를 보고, Store class 내 dbt_category 접근을 허용(멋지다!)


class InsertCsv_db(models.Model):
    """Insert CSVfile to DB"""

    order_num = models.CharField(max_length=20, primary_key=True)
    order_type = models.CharField(max_length=20)
    store_name = models.CharField(max_length=45)
    licence_num = models.CharField(max_length=20)
    start_address = models.CharField(max_length=120)
    destination_address = models.CharField(max_length=120)
    destination_detailaddress = models.CharField(max_length=80)
    payment_method = models.CharField(max_length=30)
    pickup_ornot = models.CharField(max_length=20)
    order_amount = models.CharField(max_length=45)
    delivery_fee = models.CharField(max_length=45)
    total_amount = models.CharField(max_length=45)
    store_coupon_amount = models.CharField(max_length=45)
    dbt_coupon_amount = models.CharField(max_length=45)
    dbt_coupon_name = models.CharField(max_length=30)
    dbt_coupon_code = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=45)
    order_date = models.CharField(max_length=20)
    order_time = models.CharField(max_length=20)

    objects = DataFrameManager()

    class Meta:
        db_table = "statistics_csv"
        ordering = ["-order_num"]

    def __str__(self):
        return self.store_name + "::" + self.total_amount

    def get_absolute_url(self):
        return reverse("key_statistics:SalesDetail", kwargs={"pk": self.pk})


class Question(models.Model):
    """Question Model Definition"""

    q_title = models.CharField(max_length=50)
    q_content = models.TextField(blank=True)
    q_author = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.q_title


class Answear(models.Model):
    """Answear Model Definition"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    a_title = models.CharField(max_length=50)
    a_content = models.TextField(blank=True)

    def __str__(self):
        return self.a_title


class Post(models.Model):
    """Post Model Definition"""

    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True)
    file_upload = models.FileField(upload_to="files/%Y/%m/%d", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("key_statistics:post", kwargs={"pk": self.pk})

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split(".")[-1]
