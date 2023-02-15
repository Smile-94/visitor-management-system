# Generated by Django 4.1.5 on 2023-01-23 11:31

import accounts.utils
from django.db import migrations, models
import employee.utils


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employeeinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='photo',
            field=models.ImageField(upload_to=accounts.utils.user_directory_path, validators=[employee.utils.validate_image_type, employee.utils.validate_image_file_size, employee.utils.validate_image_dimention]),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='signature',
            field=models.ImageField(upload_to=accounts.utils.user_directory_path, validators=[employee.utils.validate_image_type, employee.utils.validate_signature_image_file_size, employee.utils.validate_image_signature_dimention]),
        ),
    ]