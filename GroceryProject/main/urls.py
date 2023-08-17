
from django.conf.urls.static import static
from django.urls import path
from GroceryProject import settings

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact_us'),
    path('shop/', views.shop, name='shop'),
    path('new_products/', views.new_products, name='new_products'),
    path('sales/', views.sales, name='sales'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:pk>/', views.product, name='product_detail'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logoutUser, name='logout'),
    path('search/', views.search, name='search'),
    path('shop/<str:category>/', views.shop_category, name='shop_category'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('change_item_quantity/<int:pk>/', views.change_item_quantity, name='change_item_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)