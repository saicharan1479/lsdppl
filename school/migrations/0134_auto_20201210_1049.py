# Generated by Django 3.1.3 on 2020-12-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0133_remove_daily_data_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='dok_bank',
            name='remove',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dok_entry',
            name='remove',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
