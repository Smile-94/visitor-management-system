# Generated by Django 4.1.5 on 2023-03-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0006_remove_visitormedialink_instagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorinfo',
            name='visitor_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
