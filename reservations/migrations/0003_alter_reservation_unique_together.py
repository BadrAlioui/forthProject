# Generated by Django 5.1 on 2024-09-08 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_reservation_time'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('first_name', 'last_name', 'date_booking')},
        ),
    ]
