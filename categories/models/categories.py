from django.db import models
from core.core import CoreBaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(CoreBaseModel):
    name = models.CharField(blank=True,null=True, max_length=200)

    class Meta:
        verbose_name_plural = _("Category")

    def __str__(self):
        return self.name
    