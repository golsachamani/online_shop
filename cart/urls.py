from django.urls import path, include
from . views import *
urlpatterns = [
path('', cart_detail_view, name='cart_detail')
]    