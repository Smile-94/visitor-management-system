# Generated by Django 4.1.5 on 2023-01-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_permanentaddress_delete_parmanentaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permanentaddress',
            name='post_code',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='presentaddress',
            name='post_code',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
