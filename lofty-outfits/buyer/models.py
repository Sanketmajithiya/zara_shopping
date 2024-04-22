from django.db import models

from master.models import baseModel
from authentication.models import customersModel
from seller.models import productsModel
# Create your models here.

class cartModel(baseModel):
    customer_id = models.ForeignKey(customersModel, on_delete=models.CASCADE)
    product_id = models.ForeignKey(productsModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class ContactUSModel(baseModel):

    STATUS_CHOICES = (
        ('resolved', 'Resolved'),
        ('unresolved', 'Unresolved'),
        ('on_working', 'On Working')
    )


    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='unresolved', max_length=255)