from django.db import models
from kvapp.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=225)

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(decimal_places=None, max_digits=None, null=True, blank=True)
    discounted_price = models.IntegerField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image1 = models.FileField(upload_to='product-image', null=True, blank=True)
    image2 = models.FileField(upload_to='product-image', null=True, blank=True)
    image3 = models.FileField(upload_to='product-image', null=True, blank=True)
    image4 = models.FileField(upload_to='product-image', null=True, blank=True)
    image5 = models.FileField(upload_to='product-image', null=True, blank=True)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=225, null=True, blank=True)
    color = models.CharField(max_length=225, null=True, blank=True)
    size = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=225, null=True, blank=True)
    weight = models.CharField(max_length=225,  null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.CharField(max_length=225, null=True, blank=True)
    purchase_note = models.TextField(null=True, blank=True)
    visibility = models.CharField(max_length=225, null=True, blank=True)
    collectors_pick = models.BooleanField(default=False)
    product_reviews = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class brand(models.Model):
    brand_name = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.brand_name

class clothing(models.Model):
    cloth_name = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.cloth_name

class shoe(models.Model):
    shoe_type = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.shoe_type 

class face_and_body(models.Model):
    name = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class accessories(models.Model):
    accessory_name = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.accessory_name

class beauty(models.Model):
    beauty_product_name = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.beauty_product_name

class kids(models.Model):
    product_name = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.product_name