from django.shortcuts import render, redirect
from django.urls import reverse
from main.decorators import unauthenticated_user
from main.models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from users.models import CustomUser

# Main page.
def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})


# Shop page.
def shop(request):
    products = Product.objects.all()
    category_list = products.values_list('category', flat=True).distinct()
    search = request.GET.get('search')
    categories = request.GET.getlist('categories') 
    sorting = request.GET.get('sorting')
    if sorting:
        if sorting == 'increasing':
            products = products.order_by('price')
        elif sorting == 'decreasing':
            products = products.order_by('-price')
        elif sorting == 'top':
            products = products.order_by('-stock')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    if categories:
        for category in categories:
            products = products.filter(category=category)
    return render(request, 'main/shop.html', {'products': products, 'categories': category_list})



# Contact page.
def contact(request):
    return render(request, 'main/contact.html')


# About page.
def about(request):
    return render(request, 'main/about.html')


# New products.
def new_products(request):
    products = Product.objects.all()
    return render(request, 'main/shop-filter.html', {'products': products})


# Sales
def sales(request):
    products = Product.objects.all()
    return render(request, 'main/shop-filter2.html', {'products': products})

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


# Cart
def cart(request):
    return render(request, 'main/cart.html')


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'main/product-simple.html', {'product': product})

def profile(request):
    pass

def logoutUser(request):
    logout(request)
    return redirect('index')