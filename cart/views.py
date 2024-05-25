from django.shortcuts import render,get_object_or_404, redirect
from . cart import Cart
from products.models import Product
from . forms import AddToCartProductForm
# Create your views here.
def cart_detail_view(request):
    cart = Cart(request)
    return render(request,'cart/cart_detail.html', {'cart':cart})

def add_to_cart_view(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,pk=product_id)
    form = AddToCartProductForm(request.Post)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quintity = cleaned_data['quintity']
        cart.add(product,quintity)
    return redirect('cart:cart_detail')