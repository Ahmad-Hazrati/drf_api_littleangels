# Generated by Django 3.2.23 on 2023-11-23 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20231123_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='author',
            new_name='user',
        ),
    ]