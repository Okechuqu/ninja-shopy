from enum import Enum
from django.db import models
from core.core import CoreBaseModel
from plugins.code_generator import generate_unique_ID

ORDER_DISPLAY = ['id','status','code']

class Order(CoreBaseModel):
    class StatusChoices(models.TextChoices, Enum):
        COMPLETED = "COMP", "Completed"
        PENDING = "PEND", "Pending"
        CANCELLED = "CANC", "Cancelled"

    client = models.ForeignKey('user.Client', null=True, blank=True,
                               related_name='order_client', on_delete=models.CASCADE)
    orderitems = models.ManyToManyField(
        'orders.OrderItem', related_name='orderitem_product')
    shipping_address = models.ForeignKey(
        'user.Address', null=True, blank=True, related_name='order_address', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, null=True, blank=True, default="PEND", choices=StatusChoices.choices)
    code = models.CharField(max_length=6, null=True, blank=True,
                            editable=False, unique=True, default=generate_unique_ID)

    def _str_(self):
        return f"Order {self.id}"

    def get_total_price(self):
        total = 0
        for item in self.orderitems.all():
            price = item.product.price * item.quantity
            total += price
        return total

    # def _set_total_price(self):
    #     self.total_price = self.get_total_price()
    #     self.save()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
