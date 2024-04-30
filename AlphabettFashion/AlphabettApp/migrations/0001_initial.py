# Generated by Django 5.0 on 2023-12-28 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=1000)),
                ('product_selling_price', models.IntegerField()),
                ('product_buying_price', models.IntegerField()),
                ('product_size', models.IntegerField()),
                ('sub_category', models.CharField(choices=[('sneakers', 'SNEAKERS'), ('boots', 'BOOTS'), ('football', 'FOOTBALL SHOES'), ('loafers', 'LOAFERS'), ('slides', 'SLIDES'), ('flats', 'FLAT SHOES')], max_length=100)),
                ('product_stock', models.IntegerField()),
                ('photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_mages', to='AlphabettApp.images')),
            ],
        ),
    ]