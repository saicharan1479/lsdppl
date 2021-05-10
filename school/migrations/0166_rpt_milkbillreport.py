# Generated by Django 3.1.2 on 2021-01-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0165_rpt_consolidated'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPT_Milkbillreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routecode', models.CharField(blank=True, max_length=255, null=True)),
                ('centercode', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('ltrrate', models.FloatField(default=0.0)),
                ('net', models.FloatField(default=0.0)),
                ('noofinstallments', models.IntegerField(blank=True, null=True)),
                ('center', models.CharField(blank=True, max_length=255, null=True)),
                ('sdate', models.DateField(blank=True, null=True)),
                ('idate', models.DateField(blank=True, null=True)),
                ('installment_amt', models.FloatField(blank=True, default=0.0, null=True)),
                ('interest_amt', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
            ],
        ),
    ]