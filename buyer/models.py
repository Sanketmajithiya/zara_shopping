from django.db import models

from master.models import baseModel
# Create your models here.

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