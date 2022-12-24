from django import forms
from order.models import Orders


class OrdersForms(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'lastname', 'email', 'address', 'city', 'index', 'phone_number', 'comment']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Имя'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Фамилия'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Электронная почта'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Адрес'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Город'
            }),
            'index': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Индекс'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Телефон номер'
            }),
            'comment': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Оставьте комментарий к вашему заказу'
            })
        }
