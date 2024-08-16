from . import views 
from django.urls import path

urlpatterns = [
    path('banner/list/', views.banner_list),
    path('banner/detail/<int:id>/', views.banner_detail),
    path('banner/create/', views.banner_create),
    path('banner/delete/<int:id>/', views.banner_delete),
    path('banner/update/<int:id>/', views.banner_update),
    
    path('order/delete/<int:id>/', views.order_delete),
    path('order/list/', views.order_list),
    path('order/detail/<int:id>/', views.order_detail),
    path('order/create/', views.order_create),
    path('order/update/<int:id>/', views.order_update),
    
    path('food/list/', views.food_list),
    path('food/detail/<int:id>/', views.food_detail),
    path('food/create/', views.food_create),
    path('food/delete/<int:id>/', views.food_delete),
    path('food/update/<int:id>/', views.food_update),
    
    path('category/create/', views.category_create),
    path('category/delete/<int:id>/', views.category_delete),
    path('category/update/<int:id>/', views.category_update),
    path('category/list/', views.category_list),
    path('category/detail/<int:id>/', views.category_detail),
]