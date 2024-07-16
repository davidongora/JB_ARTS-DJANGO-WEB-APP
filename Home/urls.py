from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home/checkout', views.checkout, name='checkout'),
]
