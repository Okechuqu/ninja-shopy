from django.db import models
from core.core import CoreBaseModel
# Create your models here.

ORDER_ITEM_DISPLAY = ['id', 'client', 'product', 'quantity', 'checked_out']


class OrderItem(CoreBaseModel):

    client = models.ForeignKey('user.Client', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='order_item_client')
    product = models.ForeignKey('products.Product', null=True, blank=True,
                                on_delete=models.CASCADE, related_name='order_item_product')
    quantity = models.IntegerField(blank=True, null=True)
    checked_out = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'orderItem'

    def __str__(self):
        return f"OrderItem{self.id}"

    def get_total_price(self):
        total_price = self.product.price * self.quantity
        return total_price
