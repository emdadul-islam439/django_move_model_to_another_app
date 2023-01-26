from django.db import models

from catalog_app.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'catalog_app_product'