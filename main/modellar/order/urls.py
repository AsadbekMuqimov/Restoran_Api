
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('order/new/', views.order_create, name='order_create'),
    path('order/<int:pk>/edit/', views.order_update, name='order_update'),
    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),
]
