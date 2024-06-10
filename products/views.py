from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _

from . models import Product
from . forms import *
from cart.forms import AddToCartProductForm
class ProductListView(generic.ListView):
    #model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model =Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['context_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context
class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        pk = self.kwargs['pk']
        product = get_object_or_404(Product, id = pk )
        obj.product = product
        #messages.success(self.request,_('successfully') )
        return super().form_valid(form)
    