# Generated by Django 2.2.9 on 2020-02-10 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_postcontent_day_of_theweek'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcontent',
            old_name='day_of_theweek',
            new_name='days_of_theweek',
        ),
    ]
