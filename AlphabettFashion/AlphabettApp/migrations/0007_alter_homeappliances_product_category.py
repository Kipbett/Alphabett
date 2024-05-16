# Generated by Django 5.0 on 2024-05-03 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlphabettApp', '0006_homeappliances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeappliances',
            name='product_category',
            field=models.CharField(choices=[('kitchen_ware', 'KITCHENWARE'), ('utensils', 'UTENSILS'), ('kitchen_appliances', 'KITCHEN APPLIANCES')], max_length=20),
        ),
    ]
