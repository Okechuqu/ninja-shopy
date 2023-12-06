from django.db import models
from core.core import CoreBaseModel
from plugins.generate_filename import generate_filename
# Create your models here.

PRODUCT_DISPLAY = ['id', 'name','price','stock_quantity','category','vendor']

class Product(CoreBaseModel):
    name = models.CharField(null=True, blank=True, max_length=500)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(
        null=True, blank=True)
    category = models.ForeignKey('categories.Category', null=True, blank=True,
                                 on_delete=models.CASCADE, related_name='product_category')
    image = models.ImageField(null=True, blank=True,
                              upload_to=generate_filename)
    stock_quantity = models.IntegerField()
    vendor = models.ForeignKey('user.Vendor', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='product_vendor')
    

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name
    
