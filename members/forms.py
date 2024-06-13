from django import forms
from django.forms import ModelForm
from .models import Orders,Facturare_pers_fizica

class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"

    