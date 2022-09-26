"""selloldy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.sign_up_page),
    
    path('sign_up_perform',views.sign_up_perform),
    path('admin/', admin.site.urls),
    path('loginpage',views.about),
    path('indexpage',views.hii),
    path('pay',views.pay),
    path('login',views.login_user),
    path('chatapp',views.chatapp),
    path('add_cart',views.ad_to_cart),
    path('jsondata',views.jsondata_get),
    path('justsend',views.justsend),
    path('logout',views.delete_session),
    path('cartpage',views.cartpage),
    path('check',views.chat_contact_list),
    path('deletecart',views.deletecart),
    path('hitory',views.Transaction_history),
    path('My-product',views.myproduct),
    path('deletemyitem',views.delete_my_item),
        
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
