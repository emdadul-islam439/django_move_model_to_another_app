from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+')
