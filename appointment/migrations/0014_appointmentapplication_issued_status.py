# Generated by Django 4.1.5 on 2023-03-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0013_appointmentapplication_cancel_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentapplication',
            name='issued_status',
            field=models.BooleanField(default=False),
        ),
    ]
