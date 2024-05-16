from django.db import models

# Create your models here.

# class Images(models.Model):
#     photo = models.ImageField(upload_to='photos/')


class Product(models.Model):

    PRODUCT_CATEGORIES = (
        ('sneakers', 'SNEAKERS'),
        ('boots', 'BOOTS'),
        ('football', 'FOOTBALL SHOES'),
        ('loafers', 'LOAFERS'),
        ('slides', 'SLIDES'),
        ('flats', 'FLAT SHOES'),
    )

    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=1000)
    product_selling_price = models.IntegerField()
    product_buying_price = models.IntegerField()
    # photos = models.ForeignKey(Images, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='photos/')
    product_size = models.IntegerField()
    sub_category = models.CharField(max_length=100, choices=PRODUCT_CATEGORIES)
    product_stock = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self):
        return self.product_name + ' ' + str(self.product_size)

class Watches(models.Model):
    GENDER_SELECTION = (
        ('ladies', 'LADIES'),
        ('male', 'MALE')
    )
    
    product_name = models.CharField(max_length=100)
    product_color = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='photos/')
    product_buying_price = models.IntegerField()
    product_selling_price = models.IntegerField()
    product_gender = models.CharField(max_length=10, choices=GENDER_SELECTION)
    product_stock = models.IntegerField()
    product_likes = models.IntegerField()
    
    def __str__(self):
        return self.product_name +' '+ self.product_color


class HomeAppliances(models.Model):
    PRODUCT_SELECTION = (
        ('kitchen_ware', 'KITCHENWARE'),
        ('utensils', 'UTENSILS'),
        ('kitchen_appliances', 'KITCHEN APPLIANCES')
    )

    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='photos/')
    product_buying_price = models.IntegerField()
    product_selling_price = models.IntegerField()
    product_category = models.CharField(max_length=20, choices=PRODUCT_SELECTION)
    product_stock = models.IntegerField()
    product_likes = models.IntegerField()

    def __str__(self):
        return self.product_name