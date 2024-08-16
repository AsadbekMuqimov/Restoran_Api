from rest_framework.serializers import ModelSerializer
from main.models import Banner, Order, Food, Category

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ['title', 'image']
        
        
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'price', 'quantity' ]
        
        
        
class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = ['title', 'description', 'image']
        
        
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
        

