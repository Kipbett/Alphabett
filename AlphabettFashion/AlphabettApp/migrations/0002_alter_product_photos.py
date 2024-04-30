# Generated by Django 5.0 on 2023-12-28 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlphabettApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='AlphabettApp.images'),
        ),
    ]
