# Generated by Django 4.1.5 on 2023-03-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_appointmentapplication_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentapplication',
            name='approved_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
