# Generated by Django 5.0.7 on 2024-07-25 16:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
