from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import BannerSerializer, OrderSerializer, FoodSerializer, CategorySerializer
from main.models import Banner, Order, Food, Category



@api_view(['GET'])
def banner_list(request):
    banners = Banner.objects.all()
    serializer_data = BannerSerializer(banners, many=True) 
    return Response(serializer_data.data)

@api_view(['GET'])
def banner_detail(request, id):
    banner = Banner.objects.get(id=id)
    ser_data = BannerSerializer(banner).data
    return Response(ser_data)

@api_view(['GET'])
def banner_delete(request, id):
    banners = Banner.objects.get(id = id)
    serializer_data = BannerSerializer(banners, many=True) 
    return Response(serializer_data.data)

@api_view(['GET'])
def banner_update(request, id):
    banner = Banner.objects.get(id=id)
    ser_data = BannerSerializer(banner).data
    return Response(ser_data)

@api_view(['GET'])
def banner_create(request):
    banners = Banner.objects.all()
    serializer_data = BannerSerializer(banners, many=True) 
    return Response(serializer_data.data)






@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer_data = OrderSerializer(orders, many=True)  
    return Response(serializer_data.data)

@api_view(['GET'])
def order_detail(request, id):
    order = Order.objects.get(id=id)
    ord_data = OrderSerializer(order).data
    return Response(ord_data)

@api_view(['GET'])
def order_create(request):
    orders = Order.objects.all()
    serializer_data = OrderSerializer(orders, many=True)  
    return Response(serializer_data.data)

@api_view(['GET'])
def order_delete(request, id):
    order = Order.objects.get(id=id)
    ord_data = OrderSerializer(order).data
    return Response(ord_data)

@api_view(['GET'])
def order_update(request, id):
    order = Order.objects.get(id=id)
    ord_data = OrderSerializer(order).data
    return Response(ord_data)






@api_view(['GET'])
def food_list(request):
    foods = Food.objects.all()
    serializer_data = FoodSerializer(foods, many=True)  
    return Response(serializer_data.data)

@api_view(['GET'])
def food_detail(request, id):
    food = Food.objects.get(id=id)
    foo_data = FoodSerializer(food).data
    return Response(foo_data)

@api_view(['GET'])
def food_create(request):
    foods = Food.objects.all()
    serializer_data = FoodSerializer(foods, many=True)  
    return Response(serializer_data.data)

@api_view(['GET'])
def food_delete(request, id):
    food = Food.objects.get(id=id)
    foo_data = FoodSerializer(food).data
    return Response(foo_data)

@api_view(['GET'])
def food_update(request, id):
    food = Food.objects.get(id=id)
    foo_data = FoodSerializer(food).data
    return Response(foo_data)



@api_view(['GET'])
def category_list(request):
    categors = Category.objects.all()
    serializer_data = CategorySerializer(categors, many=True)  
    return Response(serializer_data.data)

@api_view(['GET'])
def category_detail(request, id):
    category = Category.objects.get(id=id)
    cat_data = CategorySerializer(category).data
    return Response(cat_data)

@api_view(['GET'])
def category_create(request):
    categors = Category.objects.all()
    serializer_data = CategorySerializer(categors, many=True)  
    return Response(serializer_data.data)

@api_view(['GET'])
def category_delete(request, id):
    category = Category.objects.get(id=id)
    cat_data = CategorySerializer(category).data
    return Response(cat_data)

@api_view(['GET'])
def category_update(request, id):
    category = Category.objects.get(id=id)
    cat_data = CategorySerializer(category).data
    return Response(cat_data)