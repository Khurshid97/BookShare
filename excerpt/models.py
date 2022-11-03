import email
from unicodedata import decimal
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    book_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=1000)
    book_desc = models.TextField()
    book_image = models.ImageField(null=False, blank=True)
    book_amount = models.IntegerField(blank=True)
    book_cost = models.DecimalField(max_digits=7, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.book_name
    
    @property
    def imageURL(self):
        try:
            url = self.book_image.url
        except:
            url = ''
        return url


class Customer(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=True, blank=True)
    adres = models.CharField(max_length=200, null=True)
    num = models.IntegerField(null=True)
    pochta = models.IntegerField(null=True)
    ad_info = models.TextField()
    
    def __str__(self):
        return self.first_name

class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            shipping = True
        return shipping

    

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.book_cost * self.quantity
        return total
    
    def __str__(self):
        return str(self.order.customer)

class Favourite(models.Model):
    userfav = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    productfav = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.productfav)
# Create your models here.

