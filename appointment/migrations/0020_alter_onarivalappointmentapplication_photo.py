# Generated by Django 4.1.5 on 2023-03-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0019_onarivalappointmentapplication_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onarivalappointmentapplication',
            name='photo',
            field=models.BinaryField(null=True),
        ),
    ]