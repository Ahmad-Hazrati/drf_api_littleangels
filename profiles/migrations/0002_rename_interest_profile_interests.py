# Generated by Django 3.2.23 on 2023-11-20 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='interest',
            new_name='interests',
        ),
    ]
