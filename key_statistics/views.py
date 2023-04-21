from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from . import models, forms

# Create your views here.


class DashBoardView(ListView):

    """Dash Board View Definition"""

    queryset = models.InsertCsv_db.objects.all()
    # 동일결과 : model = models.InsertCsv_db
    context_object_name = "revenues"
    template_name = "key_statistics/dashboard.html"

    # # django-pandas 사용하여 필터링
    # qs = models.InsertCsv_db.objects.all()

    # df = (
    #     qs.filter(
    #         order_date__gte="2022-11",
    #     )
    #     .filter(order_date__lte="2022-12")
    #     .to_dataframe(
    #         index="order_num",
    #     )
    # )
    # # strings to integers로 변환하여 합계
    # print(df["total_amount"].astype(int).sum())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        qs = models.InsertCsv_db.objects.all()

        df = qs.to_dataframe(
            fieldnames=["order_num", "total_amount", "order_date"],
            index="order_num",
        )
        months = [
            "2022-01",
            "2022-02",
            "2022-03",
            "2022-04",
            "2022-05",
            "2022-06",
            "2022-07",
            "2022-08",
            "2022-09",
            "2022-10",
            "2022-11",
            "2022-12",
        ]
        monthly_sales = dict()

        for month in months:
            # 월별 df 필터링 (데이터프레임 형태)
            monthly_df = df[df["order_date"].str.contains(month)]
            # strings to integers로 변환하여 합계
            monthly_amount = monthly_df["total_amount"].astype(int).sum()
            # dict자료형태인 monthly_sales에 key, value 값을 추가
            monthly_sales[month] = monthly_amount
            # 쿼리한 집합(dict type)을 context 객체에 추가한다.
            context["monthly_sales"] = monthly_sales

            # monthly_sales의 keys 값을 리스트로 변환시켜서 담음
            context["monthly_sales_month"] = list(monthly_sales.keys())
            # monthly_sales의 values 값을 리스트로 변환시켜서 담음
            context["monthly_sales_amount"] = list(monthly_sales.values())

        return context

        # <strings to integers로 변환하여 합계>
        # monthly_sales = df["total_amount"].astype(int).sum()

        # <기간 필터링 후, pandas 데이터프레임으로 변경>
        # df = qs.filter(order_date__startswith="2022-11").to_dataframe(
        #     fieldnames=["order_num", "total_amount", "order_date"],
        #     index="order_num",
        # )
        # <기간 필터링>
        # df = (
        #     qs.filter(order_date__gte="2022-11")
        #     .filter(order_date__lte="2022-12")
        #     .to_dataframe(index="order_num",)
        # )

        # 첫문자 필터링
        # df = qs.objects.filter(headline__startswith="What")

        # 쿼리한 집합을 context 객체에 추가한다.
        # context["monthly_sales"] = monthly_sales
        # context["weekly_sales"] = ##


class HomeView(ListView):

    """HomeView Definition"""

    model = models.InsertCsv_db
    paginate_by = 10
    paginate_orphans = 5
    ordering = "order_date"
    context_object_name = "revenues"
    template_name = None


class SalesDetail(DetailView):
    "sales Detail Definition"

    model = models.InsertCsv_db
    context_object_name = "revenue"
    template_name = None


class SearchView(View):

    """SearchView Definition"""

    # 파라미터로 requst.POST 값을 전달해줘야 함
    form = forms.SearchForm()


class PostView(ListView):
    "Post List Definition"
    model = models.Post
    context_object_name = "posts"
    template_name = "key_statistics/post_list.html"


class PostViewDetail(DetailView):
    "Post Detail Definition"
    model = models.Post
    context_object_name = "post"
    template_name = "key_statistics/post_detail.html"


def Question(request):
    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # question.author = request.user
            question.published_date = timezone.now()
            question.save()
            # redirect 함수에서 첫번째 파라미터는 이동해야될 view이름임
            # post_detail 뷰는 pk변수가 필요하며, pk=post.pk를 사용해서 뷰에게 값을 넘겨줌
            return redirect("key_statistics/question_detail.html", pk=pk)
    else:
        form = forms.QuestionForm()

    return render(request, "key_statistics/question_list.html", context={"form": form})


def Question_edit(request, pk):
    pass


def AnswearCreate(request, pk):
    """답변등록"""
    question = get_object_or_404(Question, pk=pk)
    # textarea에 입력된 데이터가 파이썬 객체에 담겨넘어오고, 이 값을 추출
    # request.POST.get("content")는 POST형식으로 전송된 form 데이터 항목 중 name이 content인 값을 의미함
    question.Answear_set.create(
        content=request.POST.get("content"), create_date=timezone.now()
    )

    return redirect("key_statistics:question_edit", pk=pk)
