# Generated by Django 3.0.4 on 2020-09-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Route_attached', models.CharField(max_length=255)),
            ],
        ),
    ]
