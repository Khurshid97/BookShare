import json
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {} 

    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']
    
    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Book.objects.get(id=i)
            total = (product.book_cost * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'book_name': product.book_name,
                    'slug':product.slug,
                    'book_cost':product.book_cost,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
        except: 
            pass
    return {'cartItems':cartItems, 'order':order, 'items':items}

def cartData(request):

    if request.user.is_authenticated:
        customer = request.user
        customer2, created = Customer.objects.get_or_create(first_name=customer)

        order, created = Order.objects.get_or_create(customer=customer2, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
        favorites = Favourite.objects.filter(userfav_id=request.user.id)

    else:
        

        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems':cartItems, 'order':order, 'items':items}