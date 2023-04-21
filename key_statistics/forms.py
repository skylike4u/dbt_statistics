from django import forms
from . import models


class QuestionForm(forms.ModelForm):

    """Question Form Definition"""

    class Meta:
        model = models.Question
        # fields = '__all__'
        fields = [
            "q_title",
            "q_content",
            "q_author",
        ]
        widgets = {
            "q_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "write title",
                },
            ),
            "q_content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "write content",
                },
            ),
        }


class SearchForm(forms.Form):
    order_num = forms.IntegerField(required=False)
    order_type = forms.ModelChoiceField(
        required=False,
        empty_label="any kind",
        queryset=models.InsertCsv_db.objects.all(),
    )
    store_name = forms.CharField(initial="Anywhere")
    # licence_num = forms.
    # start_address = forms.
    # destination_address = forms.
    # destination_detailaddress = forms.
    # total_amount = forms.
    # customer_phone = forms.
    # order_date = forms.
    # order_time = forms.
