from django.db import models

# Create your models here.

class auth_admin(models.Model):
    admin_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.admin_id    


class Product_name(models.Model):
    p_id = models.CharField(max_length=50, primary_key=True)
    p_name = models.CharField(max_length=100)

    def __str__(self):
        return self.p_name


class product_details(models.Model):
    product_name = models.ForeignKey(Product_name, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(default=True)
    image = models.ImageField(upload_to="admin_module/images", blank=True)
    model = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_name} : {self.model}"


