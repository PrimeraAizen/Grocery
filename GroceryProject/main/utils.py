from main.models import Product, Order, OrderItem, ShippingAddress, Customers


def get_cart(request):
    if request.user.is_authenticated:
        customer = Customers.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    
    return {'items': items, 'order': order}