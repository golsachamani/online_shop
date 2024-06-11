from django.contrib import messages
from django.utils.translation import gettext as _

from products.models import Product
class Cart(object):
    def __init__(self, request):

        """
        initialize the cart
        """
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
   

    def add(self,product,quantity=1, replace_current_quantity=False ):

        """
        add sepecified the product in card if not exist
        """
        product_id = str(product.id)
        if product_id not  in self.cart:
            self.cart[product_id] = {'quantity': 0}   
        if replace_current_quantity:
             self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            messages.success(self.request, _('product successfully add to cart'))

        self.save()

    def remove(self,product):

        """
        remove product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _('product successfully remove from cart'))
        self.save()


    def save(self):
        """
        mark session as modified to save change
        """
        self.session.modified = True
    
    # def __iter__(self):
    #     product_ids = self.cart.keys()
    #     products = Product.objects.filter(id__in=product_ids)
    #     cart = self.cart
    #     total_price = 0  # Initialize total price

    #     for p in products:
    #         item_quantity = cart[str(p.id)]['quantity']
    #         item_price = p.price  # Assuming 'price' is a field in the Product model
    #         item_total_price = item_quantity * item_price
    #         total_price += item_total_price  # Add the item's total price to the overall total
    #         item = {
    #             'product': p,
    #             'quantity': item_quantity,
    #             'total_price': item_total_price  # Include the total price for each item in the iteration
    #     }
    #     yield item

    # # After iterating through all items, yield the total price
    #     yield {'total_price': total_price}

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart
        
        
        for p in products:
            item = {
                'product': p,
                'quantity': cart[str(p.id)]['quantity'],
                'item_total_price': cart[str(p.id)]['quantity'] * p.price

                }
           
            yield item
        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session['cart']
        self.save()
    
    
        
        



    def get_total_price(self):
        total_price = 0  # Initialize total price
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for p in products:
            item_quantity = self.cart[str(p.id)]['quantity']
            item_price = p.price  # Assuming 'price' is a field in the Product model
            item_total_price = item_quantity * item_price
            total_price += item_total_price  # Add the item's total price to the overall total

        return total_price
 
    def is_empty(self):
        if self.cart:
            return False
        else:
            return True