from django.shortcuts import render, redirect
from django.urls import reverse
from main.utils import get_cart
from main.decorators import unauthenticated_user
from main.models import Product, Order, OrderItem, ShippingAddress, Customers
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from users.models import CustomUser
from django.views.decorators.csrf import csrf_exempt

# Main page.
def index(request):
    products = Product.objects.all()
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/index.html', {'products': products, 'items': items, 'order': order})

# Page for product.
def product(request, pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/product-simple.html', {'product': product, 'products': products, 'items': items, 'order': order})

# Shop page.
def shop(request):
    products = Product.objects.all()
    sorting = request.POST.get('sorting') if request.POST.get('sorting') else ''
    if sorting == 'increasing':
        products = products.order_by('price')
    elif sorting == 'decreasing':
        products = products.order_by('-price')
    elif sorting == 'top':
        products = products.order_by('-stock')
    categories = products.values_list('category', flat=True).distinct()
    category_list = request.POST.getlist('categories') if request.POST.getlist('categories') else ''
    products = products.filter(Q(category__in=category_list) if category_list else Q(category__in=categories))
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/shop.html', {'products': products, 'categories': categories, 'items': items, 'order': order, 'sorting': sorting})

# Search page.
def search(request):
    products = Product.objects.filter((Q(name__icontains=request.GET.get('q')) | Q(description__icontains=request.GET.get('q'))) & Q(category__in=request.POST.getlist('categories')) if request.POST.getlist('categories') else Q(name__icontains=request.GET.get('q')) | Q(description__icontains=request.GET.get('q')))
    sorting = request.POST.get('sorting') if request.POST.get('sorting') else ''
    category_list = products.values_list('category', flat=True).distinct()
    if sorting == 'increasing':
        products = products.order_by('price')
    elif sorting == 'decreasing':
        products = products.order_by('-price')
    elif sorting == 'top':
        products = products.order_by('-stock')
    return render(request, 'main/shop.html', {'products': products, 'categories': category_list, 'search': request.GET.get('q'), 'sorting': sorting})

# Shop page by category.
def shop_category(request, category):
    products = Product.objects.filter(category=category)
    sorting = request.POST.get('sorting') if request.POST.get('sorting') else ''
    if sorting == 'increasing':
        products = products.order_by('price')
    elif sorting == 'decreasing':
        products = products.order_by('-price')
    elif sorting == 'top':
        products = products.order_by('-stock')
    categories = products.values_list('category', flat=True).distinct()
    category_list = request.POST.getlist('categories') if request.POST.getlist('categories') else ''
    products = products.filter(Q(category__in=category_list) if category_list else Q(category__in=categories))
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/shop.html', {'products': products, 'categories': categories, 'items': items, 'order': order, 'sorting': sorting})

# New products.
def new_products(request):
    products = Product.objects.filter(new=True)
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/shop-filter.html', {'products': products, 'items': items, 'order': order})

# Page for sales.
def sales(request):
    products = Product.objects.filter(Q(sale=True) and Q(old_price__isnull=False))
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/shop-filter2.html', {'products': products, 'items': items, 'order': order})

# Page for login.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'main/login.html')
    return render(request, 'main/login.html')

# Page for registration.
@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = CustomUser.objects.filter(email=email)
        if user.exists():
            messages.info(request, 'Пользователь с таким email уже существует')
            return render(request, 'main/register.html')
        if password != password2:
            messages.info(request, 'Пароли не совпадают')
            return render(request, 'main/register.html')
        user = CustomUser.objects.create_user(email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'main/register.html')

# Logout page.
def logoutUser(request):
    logout(request)
    return redirect('index')

# Cart page.
@csrf_exempt
def cart(request):
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/cart.html', {'items': items, 'order': order})

# Adding products to cart
def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)
    order, created = Order.objects.get_or_create(customer=Customers.objects.get(user=request.user), complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return redirect('cart')

# Removing products from cart
def remove_from_cart(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    order_item.delete()
    return redirect('cart')

# Changing quantity of products in cart
def change_item_quantity(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    if request.POST.get('quantity'):
        order_item.quantity = request.POST.get('quantity')
        order_item.save()
    return redirect('cart')

def profile(request):
    pass

def checkout(request):
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    if request.user.is_authenticated:
        customer = Customers.objects.get(user=request.user)
    else:
        customer = None
    return render(request, 'main/checkout.html', {'items': items, 'order': order, 'customer': customer})

# Contact page.
def contact(request):
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/contact.html', {'items': items, 'order': order})

# About page.
def about(request):
    cart = get_cart(request)
    items = cart['items']
    order = cart['order']
    return render(request, 'main/about.html', {'items': items, 'order': order})

