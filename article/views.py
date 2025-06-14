from django.shortcuts import render
from .models import Article , Comment
# Create your views here.

def article_list(request):
    articles=Article.objects.all()
    return render(request,"articles/list.html",{"articles":articles})

def article_detail(request , pk):
    article=Article.objects.get(pk=pk)
    return render(request , "articles/detail.html",{"article":article})
