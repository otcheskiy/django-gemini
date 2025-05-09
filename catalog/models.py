from django.db import models
from django.utils.text import slugify
#from django.core.exceptions import ValidationError

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
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Генерируем только для новых объектов
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)
    
    def _generate_unique_slug(self):
        """Генерирует уникальный slug из имени, добавляя номер при необходимости"""
        base_slug = slugify(self.name)
        slug = base_slug
        num = 1
        
        while Product.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{num}"
            num += 1
            
        return slug
