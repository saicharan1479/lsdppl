# Generated by Django 3.1.3 on 2020-11-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0102_auto_20201121_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='signup',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='signup',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
