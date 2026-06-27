from django.shortcuts import render, redirect
from .models import Product, Cart, Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

def home(request):

    query = request.GET.get('search')
    category = request.GET.get('category')

    products = Product.objects.all()

    if category:
        products = products.filter(category=category)

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'home.html', {
        'products': products
    })

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, id):

    product = Product.objects.get(id=id)

    Cart.objects.create(
        product=product,
        quantity=1,
        user=request.user
    )

    return redirect('cart')
@login_required
def cart(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)
        

            return redirect('home')

    return render(request, 'login.html')

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')
def remove_from_cart(request, id):
    item = Cart.objects.get(id=id)
    item.delete()

    return redirect('cart')
def increase_quantity(request, id):
    item = Cart.objects.get(id=id)
    item.quantity += 1
    item.save()

    return redirect('cart')


def decrease_quantity(request, id):
    item = Cart.objects.get(id=id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    return redirect('cart')
def logout_user(request):
    logout(request)
    return redirect('home')
@login_required
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    if request.method == 'POST':

        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        Order.objects.create(
    user=request.user,
    name=name,
    phone=phone,
    address=address,
    total_amount=total
)
        Cart.objects.filter(
    user=request.user
).delete()

        return render(request, 'success.html')

    return render(request, 'checkout.html', {
        'total': total
    })
@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-order_date')

    return render(request, 'my_orders.html', {
        'orders': orders
    })
def forgot_password(request):
    return render(request, 'forgot_password.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')