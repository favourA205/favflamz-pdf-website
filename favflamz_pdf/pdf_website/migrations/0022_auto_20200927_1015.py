# Generated by Django 3.0.7 on 2020-09-27 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_website', '0021_auto_20200927_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationdata',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='registrationdata',
            name='is_active',
            field=models.IntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive')], default=1, help_text='1 ->Active, 0->Inactive', null=True),
        ),
        migrations.AddField(
            model_name='registrationdata',
            name='updated_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
