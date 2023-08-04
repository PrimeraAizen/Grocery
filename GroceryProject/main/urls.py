
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
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)