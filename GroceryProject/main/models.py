from django.db import models
from django.urls import reverse

from users.models import CustomUser



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    category = models.CharField(max_length=100)
    brands = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    reward_points = models.IntegerField()
    old_price = models.FloatField(blank=True, null=True)
    new = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    

    # function to return the first 2 sentences of the description
    def short_description(self):
        sentences = self.description.split('.')[0:2]
        return '.'.join(sentences) + '.'
    
class Customers(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return self.user.email


class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return str(self.id)
    
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        return sum([item.get_total() for item in order_items])
    
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        return sum([item.quantity for item in order_items])
    
    def get_absolute_url(self):
        return reverse('cart')
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'order_item'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
    
    def __str__(self):
        return self.product.name
    
    def get_total(self):
        return self.product.price * self.quantity
    
    def get_total_items(self):
        return self.product.stock * self.quantity
    
    def get_absolute_url(self):
        return reverse('cart')
    
class ShippingAddress(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'shipping_address'
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresses'
    
    def __str__(self):
        return self.user.email
    
    def get_absolute_url(self):
        return reverse('cart')