# Generated by Django 4.1.5 on 2023-03-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0012_remove_appointmentapplication_cancel_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentapplication',
            name='cancel_message',
            field=models.TextField(null=True),
        ),
    ]