# Generated by Django 4.1.5 on 2023-03-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0014_appointmentapplication_issued_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentapplication',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointmentapplication',
            name='entering_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointmentapplication',
            name='exit_time',
            field=models.TimeField(null=True),
        ),
    ]