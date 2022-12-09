from django import forms
from .models import Orders


class OrdersForms(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('name', 'lastname', 'email', 'city', 'address', 'index', 'phone_number', 'comment')
