# Generated by Django 3.1.3 on 2020-11-26 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0123_usersdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdata',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.signup'),
        ),
    ]