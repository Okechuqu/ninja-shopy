from plugins.generate_filename import generate_filename
from django.utils.translation import gettext_lazy as _
from user.models import CustomUser
from django.db import models

class Client(CustomUser):
    shipping_address = models.ManyToManyField('user.Address', related_name="client_addresses")
    profile_img  = models.ImageField(blank=True, null=True, upload_to=generate_filename)

    class Meta:
        verbose_name_plural = _('Client')

    def __str__(self):
        return self.username
    