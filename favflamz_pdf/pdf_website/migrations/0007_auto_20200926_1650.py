# Generated by Django 3.0.7 on 2020-09-26 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_website', '0006_auto_20200926_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationdata',
            old_name='first_name',
            new_name='full_name',
        ),
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
