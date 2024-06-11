from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . forms import OrderForm
from .models import *
from cart.cart import Cart

# def Order_Create_View(request):
#     form = OrderForm()
#     if request.method == 'POST':
#         form = OrderForm(request.POST,)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = request.user
#             form.save()
  
#         else:
#             form = OrderForm()

#     return render(request, 'orders/order_create.html',{'form': form})
   
@login_required
def Order_Create_View(request):
    cart = Cart(request)
    form = OrderForm()
    if len(cart) == 0:
        messages.warning(request,'empty cart')
        return redirect('product:product_list')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Process the valid form data and save it to the database
            form_instance = form.save(commit=False)
            form_instance.user = request.user
            form_instance.save()

            for item in cart:
                product_obj = item['product']
                OrderItem.objects.create(order =form_instance , product = product_obj, price= product_obj.price, quantity=item['quantity'], ) 

            cart.clear()
            messages.success(request, 'record your order successfully')
            return redirect('order:order_create')  # Redirect to a success page or another view
        request.user.first_name = form_instance.user
        request.user.last_name = form_instance.last_name
        request.user.save()
    else:
    #     # If the request method is not POST or the form is not valid, create a new instance of the form
        form = OrderForm()

    return render(request, 'orders/order_create.html', {'form': form})
