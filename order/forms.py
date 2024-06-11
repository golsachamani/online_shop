from django  import forms
from . models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'order_notes',]
        widgets = {'address': forms.Textarea(attrs={'row':5})}