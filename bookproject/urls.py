"""bookproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from excerpt.sitemaps import BookSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

from excerpt import views as base_views

sitemaps = {
    'books': BookSitemap,
    'static': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('excerpt.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('about', base_views.about, name='about'),
    path('home', base_views.homeStore, name='home'),
    path('register', base_views.registerPage, name='register'),
    path('logout', base_views.logoutUser, name='logout'),
    path('javoblar', base_views.javoblar, name='javoblar'),
    path('cart', base_views.cart, name='cart'),
    path('update_item', base_views.updateItem, name='update_item'),
    path("robots.txt", base_views.robotsView, name='robots'), 
] 
urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT) 