from django.contrib.sitemaps import Sitemap
from .models import Book
from django.urls import reverse


class BookSitemap(Sitemap):

    def items(self):
        return Book.objects.all()

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['about', 'home', 'register', 'logout', 'javoblar', 'cart', 'update_item']

    def location(self, item):
        return reverse(item)