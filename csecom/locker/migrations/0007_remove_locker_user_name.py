# Generated by Django 4.0 on 2023-07-13 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0006_locker_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locker',
            name='user_name',
        ),
    ]
