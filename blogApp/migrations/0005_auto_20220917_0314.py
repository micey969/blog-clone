# Generated by Django 3.2.5 on 2022-09-17 03:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_auto_20220916_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 3, 14, 12, 988358, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 3, 14, 12, 987894, tzinfo=utc)),
        ),
    ]
