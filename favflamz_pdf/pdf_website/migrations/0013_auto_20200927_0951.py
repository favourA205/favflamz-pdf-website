# Generated by Django 3.0.7 on 2020-09-27 08:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_website', '0012_auto_20200927_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 27, 8, 51, 20, 559288, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='updated_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 27, 8, 51, 20, 559288, tzinfo=utc), null=True),
        ),
    ]
