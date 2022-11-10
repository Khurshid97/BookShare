from itertools import product
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import json
import telegram_send

from .utils import cartData, cookieCart
# Create your views here.

def homeStore(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    categor = request.GET.get('category')

    if categor == None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(category__name=categor)

    search_input = request.GET.get('Qidiruv-maydoni') or ''
    if search_input:
        books = Book.objects.filter(book_name__icontains=search_input)

    categories = Category.objects.all()

    context = { 'books':books, 'cartItems':cartItems, 'order':order, 'items':items, 'categories':categories, 'search_input':search_input
    }

    return render(request, 'excerpt/home.html', context)

def cart(request):
    customer = request.user
    customer2, created = Customer.objects.get_or_create(first_name=customer)
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items'] 

    if request.method == 'GET':
        founder = request.GET.get('finder')
        if founder == 'sleep':  
            l_item = {}
            for item in items:
                l_item[item.product.book_name] = item.quantity
            # print(founder)
            if order.get_cart_total > 0:
                telegram_send.send(messages=[f'Eski xaridor \n Ism: {customer.username} \n Familya: {customer.last_name} \n Email: {customer.email} \n Manzil: {customer2.adres} \n Telefon raqami: {customer2.num} \n Kitob nomi va soni: {l_item} \n Umumiy narx: {order.get_cart_total}'])
                return redirect('javoblar')
    context = {'items':items, 'order':order, 'cartItems':cartItems}

    return render(request, 'excerpt/cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action'] 

    customer = request.user
    product = Book.objects.get(id=productId)

    customer2, created = Customer.objects.get_or_create(first_name=customer)
    order, created = Order.objects.get_or_create(customer=customer2, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
        
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save() 

    if orderItem.quantity <= 0 or action == 'deleter':
        orderItem.delete()

    if action == 'favorite':
        favorite, created = Favourite.objects.get_or_create(userfav=customer, productfav=product)

    return JsonResponse('Item is added', safe=False)

def registerPage(request):

    if request.user.is_authenticated:
        customer = request.user
        customer2, created = Customer.objects.get_or_create(first_name=customer)
        order, created = Order.objects.get_or_create(customer=customer2, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        if request.method == 'POST':
            form = CreatingUserForm(request.POST)
            if form.is_valid():
                form.save()
                
                first_name = form['username'].value()
                password = form['password1'].value()
                last_name = form['last_name'].value()
                mail = form['email'].value()
                adres = form['adres'].value()
                numr = form['numr'].value()
                customer2, created = Customer.objects.get_or_create(first_name=first_name, last_name=last_name, email=mail, adres=adres, num=numr)
                customer2.save()

                cookieData = cookieCart(request)
                items = cookieData['items']

                mahsulot_nomi = []
                order = Order.objects.create(customer=customer2, complete=False)
                for item in items:
                    product = Book.objects.get(id=item['product']['id'])
                    orderItem = OrderItem.objects.create(
                        product=product,
                        order=order,
                        quantity=item['quantity']
                    )
                    mahsulot_nomi.append([product, item['quantity']])

                telegram_send.send(messages=[f'Yangi foydalanuvchi \n Ism: {first_name} \n Familya: {last_name} \n Email: {mail} \n Manzil: {adres} \n Telefon raqami: {numr} \n Kitob nomi va soni: {mahsulot_nomi} \n Umumiy narx: {order.get_cart_total}'])
                
                user = authenticate(request, username=first_name, password=password)
                if user is not None:
                    login(request, user)
                    
                return redirect('javoblar')
            else:
                print('xatolik')
                return redirect('register')
        else:
            data = cartData(request)
            cartItems = data['cartItems']
            order = data['order']
            items = data['items'] 
            form = CreatingUserForm()
        

    context = {'items':items, 'order':order, 'cartItems':cartItems, 'form':form}

    return render(request, 'excerpt/register.html', context)

def about(request):
    context = {}
    return render(request, 'excerpt/about.html', context)

def javoblar(request):
    return render(request, 'excerpt/javob.html')

def page(request, pk):
    if request.user.is_authenticated:
        customer = request.user
        customer2, created = Customer.objects.get_or_create(first_name=customer)
        order, created = Order.objects.get_or_create(customer=customer2, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    book = Book.objects.get(id=pk)
    books = Book.objects.all()
    context = {'book':book, 'books':books, 'cartItems': cartItems}

    return render(request, 'excerpt/page.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# Main pages