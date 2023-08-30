from main.models import Product, Order, OrderItem, ShippingAddress, Customers
from django.core.paginator import Paginator



def get_cart(request):
    if request.user.is_authenticated:
        customer = Customers.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    
    return {'items': items, 'order': order}

def paginate(request, products):
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_products = paginator.get_page(page_number)
    return page_products
