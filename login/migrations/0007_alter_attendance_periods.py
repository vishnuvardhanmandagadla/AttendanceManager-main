# Generated by Django 5.0.4 on 2024-04-15 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_rename_dates_calender_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='periods',
            field=models.IntegerField(default=9, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
    ]
