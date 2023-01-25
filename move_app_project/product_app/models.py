from django.db import models

from catalog_app.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)