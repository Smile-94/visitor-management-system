# Generated by Django 4.1.5 on 2023-03-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_remove_appointment_cancel_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='visiting_hour',
            field=models.DurationField(blank=True, null=True),
        ),
    ]