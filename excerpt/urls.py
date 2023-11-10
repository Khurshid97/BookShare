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
from . import views
from .views import BookListApiView, CategoryListApiView

urlpatterns = [
    path('', views.homeStore, name='home'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('javoblar/', views.javoblar, name='javoblar'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('page/<str:pk>/', views.page, name='page'),
    path('update_item/', views.updateItem, name='update_item'),

    # Your existing URLs
    path('api/books/', BookListApiView.as_view(), name='book-list-api'),
    path('api/categories/', CategoryListApiView.as_view(), name='category-list-api'),
]
