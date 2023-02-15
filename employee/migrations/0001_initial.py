# Generated by Django 4.1.5 on 2023-01-22 22:32

import accounts.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import employee.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpoloyeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('HR', 'Human Resource'), ('administrative', 'Administrative'), ('software development', 'Software Development'), ('QA', 'Quality Assurance'), ('project management', 'Project Management'), ('Product Management', 'Product Management'), ('design', 'Design'), ('devOps', 'DevOps'), ('customer support', 'Customer Support'), ('marketing', 'Marketing'), ('IT', 'Information Technology')], max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('joining_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=15)),
                ('national_id', models.CharField(max_length=50)),
                ('passport_no', models.CharField(blank=True, max_length=50, null=True)),
                ('driving_license', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(height_field=300, upload_to=accounts.utils.user_directory_path, validators=[employee.utils.validate_image_type, employee.utils.validate_image_file_size], width_field=300)),
                ('signature', models.ImageField(height_field=80, upload_to=accounts.utils.user_directory_path, validators=[employee.utils.validate_image_type, employee.utils.validate_signature_image_file_size], width_field=300)),
                ('info_of', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
