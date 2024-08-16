from django.shortcuts import render, get_object_or_404, redirect
from main.models import Food
from .forms import FoodForm

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'food_detail.html', {'food': food})

def food_create(request):
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm()
    return render(request, 'food_form.html', {'form': form})

def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            food = form.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm(instance=food)
    return render(request, 'food_form.html', {'form': form})

def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        food.delete()
        return redirect('food_list')
    return render(request, 'food_confirm_delete.html', {'food': food})
