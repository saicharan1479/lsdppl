# Generated by Django 3.0.4 on 2020-09-29 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20200929_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
