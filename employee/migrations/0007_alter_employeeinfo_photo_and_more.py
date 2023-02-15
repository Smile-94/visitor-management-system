# Generated by Django 4.1.5 on 2023-02-14 11:32

from django.db import migrations, models
import employee.utils


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_designationinfo_remove_employeeinfo_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='photo',
            field=models.ImageField(upload_to=employee.utils.user_directory_path),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='signature',
            field=models.ImageField(upload_to=employee.utils.user_directory_path),
        ),
    ]
