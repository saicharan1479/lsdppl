# Generated by Django 3.1.2 on 2021-02-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0233_auto_20210219_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rcode', models.CharField(max_length=255, unique=True)),
                ('rname', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='remove',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]