# Generated by Django 3.0.7 on 2020-09-27 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_website', '0013_auto_20200927_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdata',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='updated_on',
        ),
    ]