from django.utils.translation import gettext_lazy as _
from django.db import models
from core.core import CoreBaseModel


class Address(CoreBaseModel):
    address = models.CharField(null=True, blank=True, max_length=500)
    is_current = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _('Address')

    def __str__(self):
        return self.address
