from django.urls import path
from .views import item_list
from .views import checkout, products
app_name = 'core'

urlpatterns = [
    path('', item_list, name='item_list'),
    path('checkout/', checkout, name='checkout'),
    path('product/', products, name='product')
]