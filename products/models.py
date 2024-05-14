from django.db import models
from django.shortcuts import render, reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_creat = models.DateField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args =[self.id])


class Comment(models.Model):

    STAR_CHOICE =[
        ('1', 'very bad'), ('2', 'bad'), ('3','normal'), ('4', 'good'), ('5', 'perfect'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='comments')
    stars = models.CharField(max_length=10, choices=STAR_CHOICE)
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modiefied = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])