
from products.models import Product
class Cart:
    def __init__(self, request):

        """
        intitialize the cart
        """
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self,product ,quintity):

        """
        add sepecified the product in card if not exist
        """
        product_id = str(product.id) 
        if product_id not  in self.card:
            self.card['product_id'] = {'quintity': quintity}   
        else:
            self.card['product']['quintity'] += quintity
        self.save()
    def remove(self,product):

        """
        remove product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart['product_id']
        self.save()


    def save(self):
        """
        mark session as modified to save change
        """
        self.session.modified = True   
    def __iter__(self):
        product_ides = self.cart.keys()
        products = Product.objects.filter(id__in=product_ides)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product
        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart.keys())
    
    def clear(self):
        del self.session['cart']
        self.save()
    
    def get_total_price(self):
         product_ides = self.cart.keys()
         products = Product.objects.filter(id__in=product_ides)
         return sum([product.price for product in products])