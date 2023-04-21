from django.db import models
from core import models as core_model
from django.urls import reverse


# 이벤트에 대한 정보 class
class Event_info(core_model.TimeStampedModel):

    """Event Information Definition"""

    event_name = models.CharField(max_length=30)
    event_description = models.CharField(max_length=100, blank=True)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_result = models.TextField("Event Result", blank=True)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"pk": self.pk})


# 이벤트의 사진/이미지를 모으는 class
class Event_image(core_model.TimeStampedModel):
    """Event Image Definition"""

    event_info = models.ForeignKey(
        "Event_info", related_name="event_info", on_delete=models.CASCADE
    )
    image_photo = models.ImageField(upload_to="images", blank=True)
    image_title = models.CharField("TITLE", max_length=30)
    image_description = models.CharField("Image Description", max_length=100)
    upload_dt = models.DateTimeField("upload Date", auto_now_add=True)

    class Meta:
        ordering = ("image_title",)

    def __str__(self):
        return self.image_title

    def get_absolute_url(self):
        return reverse("events:image_detail", kwargs={"pk": self.pk})
