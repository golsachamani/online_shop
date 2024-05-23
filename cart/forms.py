from django import forms

class AddToCartProductForm(forms.Form):
    QUINTITYU_CHOICES =[(i,str(i)) for i in range(1,30)]
    quintity = forms.TypedChoiceField(choices=QUINTITYU_CHOICES, coerce=int )