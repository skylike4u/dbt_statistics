# Generated by Django 2.2.5 on 2023-04-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key_statistics', '0004_question_q_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('head_image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
