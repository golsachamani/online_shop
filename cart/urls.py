from django.urls import path, include
from . views import *
app_name = 'cart'
urlpatterns = [
path('', cart_detail_view, name='cart_detail')
]    