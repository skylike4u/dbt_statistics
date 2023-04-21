import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from key_statistics.models import InsertCsv_db

with open(
    "C:/Users/SAMSUNG/dbt_revenue/total_revenue_20221220.csv"
) as csv_file_InsertCsv_db:
    rows = csv.reader(csv_file_InsertCsv_db)
    next(rows, None)  # csv파일의첫번째행인 테이블 header(컬럼명)를 제외하고 추가하겠음
    # ID를 체크해보고, 존재하지 않는 rows를 추가하하는 조건문을 넣을 것(예상)
    for row in rows:
        InsertCsv_db.objects.create(
            order_num=row[0],
            order_type=row[1],
            store_name=row[2],
            licence_num=row[3],
            start_address=row[4],
            destination_address=row[5],
            destination_detailaddress=row[6],
            payment_method=row[7],
            pickup_ornot=row[8],
            order_amount=row[9],
            delivery_fee=row[10],
            total_amount=row[11],
            store_coupon_amount=row[12],
            dbt_coupon_amount=row[13],
            dbt_coupon_name=row[14],
            dbt_coupon_code=row[15],
            customer_phone=row[16],
            order_date=row[17],
            order_time=row[18],
        )
        print(row)
