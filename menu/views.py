from django.shortcuts import render
from .models import Category
# Create your views here.

def category_view(request):
    categories = Category.objects.all()  # دریافت همه دسته‌بندی‌ها
    return render(request, 'menu/categories.html', {'categories': categories})