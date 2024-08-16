# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.banner_list, name='banner_list'),
    path('banner/<int:pk>/', views.banner_detail, name='banner_detail'),
    path('banner/new/', views.banner_create, name='banner_create'),
    path('banner/<int:pk>/edit/', views.banner_update, name='banner_update'),
    path('banner/<int:pk>/delete/', views.banner_delete, name='banner_delete'),
]
