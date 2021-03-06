# Generated by Django 3.0.7 on 2020-09-26 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_website', '0004_auto_20200926_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 26, 11, 28, 16, 627677, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='updated_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 26, 11, 28, 16, 628677, tzinfo=utc), null=True),
        ),
    ]
