# Generated by Django 3.0.7 on 2020-09-26 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_website', '0008_registrationdata_subject_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationdata',
            old_name='subject_name',
            new_name='name_of_subject',
        ),
    ]
