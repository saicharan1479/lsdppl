# Generated by Django 3.1.2 on 2020-11-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0077_deposit_depositno'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_data',
            name='ltrs',
            field=models.FloatField(default=0.0),
        ),
    ]
