# Generated by Django 5.0.7 on 2024-08-21 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0058_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='Product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
