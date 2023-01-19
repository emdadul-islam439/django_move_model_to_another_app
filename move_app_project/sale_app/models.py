from django.db import models

from catalog_app.models import Product

# Create your models here.
class Sale(models.Model):
    created = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)