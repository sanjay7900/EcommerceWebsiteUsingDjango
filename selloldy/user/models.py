from distutils.command.upload import upload
from django.db import models
from PIL import Image


# Create your models here.
class Userlogin(models.Model):
    Email=models.EmailField(unique=True)
    password=models.CharField(max_length=70)
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=90)
    village_post=models.CharField(max_length=90)
    contact=models.CharField(max_length=10)
class Product_info(models.Model):
    product_name=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="product_image")  
    product_price=models.FloatField(max_length=100)
    product_brand=models.CharField(max_length=70)
    product_cat=models.CharField(max_length=80)
    provider_id=models.IntegerField()
    status=models.CharField(max_length=10)
class add_to_cart(models.Model):
    product_name=models.TextField()
    product_price=models.FloatField()   
    product_id=models.IntegerField()
    who_is_to_add_id=models.IntegerField()
class chat_contact(models.Model):
    from_contact=models.IntegerField()
    to_contact=models.IntegerField()
    name_of_contact=models.TextField()
class chat_messages(models.Model):
    from_name=models.TextField()
    from_id=models.IntegerField()
    message=models.TextField()
    to_name=models.TextField()
    to_id=models.IntegerField()
    
    time_of=models.DateTimeField(auto_now=True)
    
class paymentHistory(models.Model):
    payment_id=models.IntegerField()
    order_id=models.IntegerField()
    signature=models.CharField(max_length=50)
    product_id=models.IntegerField()
    Buy_to_id=models.IntegerField()
    sold_to_id=models.IntegerField()
    
        
           
    




