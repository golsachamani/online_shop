from django.urls import path, include
from . views import *
app_name ='cart'
urlpatterns = [
path('', cart_detail_view, name='cart_detail'),
path('add/<int:product_id>/', add_to_cart_view, name='cart_add'),
path('remove/<int:product_id>/', cart_remove_view, name='cart_remove'),
] 

   
