from django.contrib import admin
from .models import Orders, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'lastname', 'email',
                    'address', 'index', 'city', 'phone_number',
                    'created', 'updated']
    list_filter = ['phone_number', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Orders, OrderAdmin)
