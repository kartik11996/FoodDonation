# Generated by Django 3.1 on 2020-09-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0010_customuser_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reciever',
            field=models.BooleanField(default='False'),
        ),
    ]
