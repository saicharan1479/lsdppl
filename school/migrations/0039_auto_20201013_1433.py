# Generated by Django 3.1.2 on 2020-10-13 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0038_auto_20201013_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily_data',
            old_name='datefrom',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='daily_data',
            old_name='shift_from',
            new_name='shift_loc',
        ),
        migrations.RemoveField(
            model_name='daily_data',
            name='dateto',
        ),
        migrations.RemoveField(
            model_name='daily_data',
            name='shift_to',
        ),
    ]
