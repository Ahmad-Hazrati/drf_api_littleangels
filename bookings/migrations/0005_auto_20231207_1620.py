# Generated by Django 3.2.23 on 2023-12-07 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='add_to_guest',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='number_of_people',
        ),
    ]
