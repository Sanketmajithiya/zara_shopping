from django.db import models
from master.models import baseModel
from authentication.models import customersModel
from seller.models import productsModel 
from master.utils.LO_UNIQUE.generate_order_id import generate_unique_order_id

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
    

class Order(models.Model):
    order_id = models.CharField(max_length=100, blank=True, unique=True)
    customer_name = models.CharField(max_length=100, blank=True)
    customer_email = models.EmailField(max_length=254, blank=True)
    shipping_address = models.TextField(blank=True)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    
    def __str__(self):
        return f"Order {self.id}"
        
    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
            print(self.order_id)        
        super(Order, self).save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product_name} ({self.quantity})"
    

class MyOrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(productsModel,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product_id}_{self.quantity}"



