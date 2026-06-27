from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart, name='cart'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, 
    name='remove_from_cart'),
    path('increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
path('decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
path('logout/', views.logout_user, name='logout'),
path('checkout/', views.checkout, name='checkout'),
path('my-orders/', views.my_orders, name='my_orders'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
]