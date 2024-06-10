from django.shortcuts import render

# Create your views here.
def Order_Create_View(request):
    return render(request, 'orders/order_create.html')
