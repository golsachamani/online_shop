from django.urls import path
from . views import *
urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
]