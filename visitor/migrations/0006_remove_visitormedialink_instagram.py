# Generated by Django 4.1.5 on 2023-03-20 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_visitormedialink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitormedialink',
            name='instagram',
        ),
    ]
