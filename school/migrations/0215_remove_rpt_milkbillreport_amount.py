# Generated by Django 3.1.2 on 2021-02-02 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0214_rpt_milkbillreport_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='amount',
        ),
    ]
