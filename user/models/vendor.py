from plugins.generate_filename import generate_filename
from django.utils.translation import gettext_lazy as _
from user.models import CustomUser
from django.db import models


class Vendor(CustomUser):
    shop_name = models.CharField(max_length=150, null=True, blank=True)
    shop_address = models.ForeignKey(
        'user.Address', related_name="vendor_addresses", on_delete=models.CASCADE, null=True, blank=True)
    shop_img = models.ImageField(
        blank=True, null=True, upload_to=generate_filename)
    category = models.ForeignKey('categories.Category', null=True, blank=True,
                                 related_name='vendor_category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _('vendors')

    def __str__(self):
        return self.username
