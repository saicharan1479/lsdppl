# Generated by Django 3.1.2 on 2021-01-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0184_auto_20210123_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='centre_code',
            field=models.IntegerField(),
        ),
    ]
