# Generated by Django 3.1.2 on 2021-01-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0204_auto_20210129_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='rcode',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='rname',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
