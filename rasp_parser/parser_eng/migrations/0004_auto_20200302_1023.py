# Generated by Django 3.0.3 on 2020-03-02 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_eng', '0003_auto_20200229_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_rasp',
            name='date_from',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 3, 2, 10, 23, 34, 443319)),
        ),
        migrations.AddField(
            model_name='group_rasp',
            name='date_to',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 3, 2, 10, 23, 34, 443319)),
        ),
    ]
