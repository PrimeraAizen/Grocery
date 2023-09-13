
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
    path(r'^activate/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:pk>/', views.product, name='product_detail'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logoutUser, name='logout'),
    path('search/', views.search, name='search'),
    path('shop/<str:category>/', views.shop_category, name='shop_category'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('change_item_quantity/', views.change_item_quantity, name='change_item_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_cart/', views.update_cart, name='update_cart'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)