# Generated by Django 3.1 on 2020-08-17 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0006_auto_20200817_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_type',
            new_name='donor',
        ),
    ]