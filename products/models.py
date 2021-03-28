from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null = True, blank = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default= now)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.user.username+ ' commented on '+ self.product.name

    class Meta:
        ordering = ['-timestamp']
