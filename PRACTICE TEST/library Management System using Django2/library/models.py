from django.db import models
from django.utils import timezone

# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=50)
    
    class Meta:
        unique_together = ['role']
        
    def __str__(self):
        return self.role
    
    
class Client(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=50)
    mobile = models.BigIntegerField()
    password = models.CharField(blank=True,max_length=20)
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
    def save(self,*args,**kwargs):
        self.password = self.mobile
        
        super(Client,self).save(*args,**kwargs)
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date =  models.DateField(default=timezone.now())
    is_in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class BookRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    renewal_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.client.firstname} - {self.book.title}"