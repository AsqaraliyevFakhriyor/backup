from django.contrib import admin
from .models import Collection, Product, Order, OrderItem, Cart, CartItem, Address, Customer

# Register your models here.
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Address)
admin.site.register(Customer)