# Generated by Django 5.0.7 on 2024-08-19 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_product_garanti'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Bime',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.bime'),
        ),
    ]
