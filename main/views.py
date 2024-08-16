from django.shortcuts import render
from main.models import Banner,  Order, Category, Food


def index(request):
    banners = Banner.objects.all()
    foods = Food.objects.all()
    order = Order.objects.all()
    category = Category.objects.all()
    
    
    context = {
        'banners': banners,
        'food': foods,
        'order': order,
        'category': category,
    }
    
    
    return render(request, 'front/index.html', context)


