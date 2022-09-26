from django.contrib import admin
from numpy import product
from .models import Product_info
from .models import Userlogin
@admin.register(Product_info)

# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_image','product_price','provider_id','product_brand','product_cat']
@admin.register(Userlogin)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','Email','password','contact','village_post','city']