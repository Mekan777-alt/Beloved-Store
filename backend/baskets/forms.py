from django import forms
from .models import Orders


class OrdersForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Имя'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Фамилия'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Электронная почта'}))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Город'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Адрес'}))
    index = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Индекс'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Телефон номер'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Оставьте комментарий к вашему заказу'}))

    class Meta:
        model = Orders
        fields = ('name', 'lastname', 'email', 'city', 'address', 'index', 'phone_number', 'comment')
