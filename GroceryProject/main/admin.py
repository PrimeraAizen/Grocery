from django.contrib import admin

from main.models import Product, Order, Profile, OrderItem, ShippingAddress



# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
