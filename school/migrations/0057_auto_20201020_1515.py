# Generated by Django 3.1.2 on 2020-10-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0056_auto_20201020_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='ifsc',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='route_code',
        ),
        migrations.AddField(
            model_name='village',
            name='code',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
