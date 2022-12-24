from django import forms
from . models import product

class productForm(forms.ModelForm):
    class meta:
        models=product
        fields="__all__"

