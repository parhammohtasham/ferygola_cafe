from django.shortcuts import render
from .models import Category, Food
# Create your views here.

def category_view(request):
    categories = Category.objects.all()   #دریافت همه دسته‌بندی‌ها
    return render(request, 'menu/categories.html', {'categories': categories})

def food_list(request, pk):
    foods = Food.objects.filter(default_category=pk)
    return render(request, 'menu/food_list.html', {'foods': foods ,'pk': pk})
