from unicodedata import decimal
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    upc = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    cost= models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name