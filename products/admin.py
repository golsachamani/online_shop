from django.contrib import admin
from .models import Product, Comment

class OfferPropertyInline(admin.TabularInline):
    model = Comment
    fields = ['stars', 'author', 'active', 'body',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [OfferPropertyInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['stars', 'author', 'active', 'body',]