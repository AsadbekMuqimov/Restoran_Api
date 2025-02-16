from django import forms
from main.models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['title', 'description', 'image']
