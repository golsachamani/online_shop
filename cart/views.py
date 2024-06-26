from django.shortcuts import render,get_object_or_404, redirect,reverse
from . cart import Cart
from products.models import Product
from . forms import AddToCartProductForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

#Create your views here.
def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity':item['quantity'],
            'inplace':True,
        })
    cart.save()
    return render(request,'cart/cart_detail.html', {'cart':cart})

@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
     
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity =cleaned_data['quantity']
        cart.add(product,quantity,replace_current_quantity=cleaned_data['inplace'])
    return  HttpResponseRedirect(reverse('cart:cart_detail'))


def cart_remove_view(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return  HttpResponseRedirect(reverse('cart:cart_detail'))
@require_POST
def clear_cart(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, 'clear successfully')
    else:
        messages.warning(request, 'your cart already empty')
    return redirect('product:product_list')


