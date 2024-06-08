from django import forms

class AddToCartProductForm(forms.Form):
    QUINTITYU_CHOICES =[(i,str(i)) for i in range(1,31)]
    quantity = forms.TypedChoiceField(choices=QUINTITYU_CHOICES, coerce=int )
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)