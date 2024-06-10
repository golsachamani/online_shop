from django.db import models
from django.shortcuts import render, reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

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
        return reverse('product:product_detail', args=[self.id])

class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager,self).get_queryset().filter(active=True)


class Comment(models.Model):

    STAR_CHOICE =[
        ('1', _('very bad')), ('2', _('bad')), ('3',_('normal')), ('4', _('good')), ('5', _('perfect')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name= _('comment text'))
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='comments',)
    stars = models.CharField(max_length=10, choices=STAR_CHOICE, verbose_name= ' your score?')
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modiefied = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #manager
    objects = models.manager
    active_comment_manager = ActiveCommentManager()
    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.product.id])