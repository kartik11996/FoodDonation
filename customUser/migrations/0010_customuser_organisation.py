# Generated by Django 3.1 on 2020-08-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0009_auto_20200822_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='organisation',
            field=models.BooleanField(default='False'),
        ),
    ]