# Generated by Django 5.0.7 on 2024-08-14 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
    ]
