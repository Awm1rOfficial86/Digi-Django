# Generated by Django 5.0.7 on 2024-08-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0044_remove_product_color1_remove_color2_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Img1',
            field=models.ImageField(blank=True, null=True, upload_to='upload/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='Img2',
            field=models.ImageField(blank=True, null=True, upload_to='upload/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='Img3',
            field=models.ImageField(blank=True, null=True, upload_to='upload/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='Img4',
            field=models.ImageField(blank=True, null=True, upload_to='upload/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='Img5',
            field=models.ImageField(blank=True, null=True, upload_to='upload/products/'),
        ),
    ]
