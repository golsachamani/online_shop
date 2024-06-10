from django.urls import path, include

from . views import *
app_name = 'order'
urlpatterns = [path('create/', Order_Create_View, name='order_create')
   
]