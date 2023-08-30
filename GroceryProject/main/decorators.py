from django.shortcuts import redirect
from main.utils import get_cart
# checks if user is authenticated
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

# checks if cart is not empty
def cart_not_empty(view_func):
    def wrapper_func(request, *args, **kwargs):
        cart = get_cart(request)['items']
        if cart:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('index')
    return wrapper_func