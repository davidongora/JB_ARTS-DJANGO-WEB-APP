from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home/checkout/<str:product_type>/<int:product_id>/', views.checkout, name='checkout'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
]
