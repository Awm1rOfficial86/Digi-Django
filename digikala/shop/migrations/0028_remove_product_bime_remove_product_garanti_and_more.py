# Generated by Django 5.0.7 on 2024-08-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_alter_product_bime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Bime',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Garanti',
        ),
        migrations.AlterField(
            model_name='category',
            name='Name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='news',
            name='Title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Bime',
        ),
        migrations.DeleteModel(
            name='Garanti',
        ),
    ]
