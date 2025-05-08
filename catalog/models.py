from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    code_1c = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name