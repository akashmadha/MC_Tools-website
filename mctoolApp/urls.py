"""
URL configuration for mctool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('',v.navbar),
    path('FAQpage',v.Faqpage, name='Faqpage'),
    path('products',v.products, name='products'),
    # path('Paving_Breaker/<int:pb_id>/', v.Paving_Breaker, name='Paving_Breaker'),
    path('pavingbreaker/<int:pb_id>/specifications/', v.PavingBreaker_Specification, name='pavingbreaker_specifications'),
   
    path('pavingb_list/', v.pavingb_list, name='pavingb_list'),

    path('product/<int:pd_id>/', v.product_detail, name='product_detail'),
    path('product_list/', v.product_list, name='product_list'),

    path('productname/', v.productname, name='product_name'),  # Product list
    path('productSPE/<int:spe_id>/', v.productSPE, name='productSPE'),  # Product details


    path('proname/', v.proname, name='proname'),  # Product list
    path('spe/<int:spe_id>/', v.spe, name='spe'),  # Product details

]
