# Generated by Django 3.0.6 on 2020-06-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contact_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pin_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='resources',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(null=True),
        ),
    ]