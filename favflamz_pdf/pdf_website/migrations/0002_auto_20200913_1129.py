# Generated by Django 3.0.7 on 2020-09-13 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationdata',
            old_name='username',
            new_name='full_name',
        ),
    ]
