from django.shortcuts import render
from .models import Article , Comment
from django.http import HttpResponse
# Create your views here.

def article_list(request):
    articles=Article.objects.all()
    return render(request,"articles/list.html",{"articles":articles})

def article_detail(request , pk):
    user=
    article=Article.objects.get(pk=pk)
    
    form=Comment()
    if request.method =="POST":
        form=Comment(request.POST)
        if comment.is_valid():
            article=Comment.cleaned_data["article"]
            comment=Comment.cleaded_data["comment"]
            writer=Comment.cleaned_data["writer"]
            new_comment=Comment(article=article , comment=comment , writer=writer)
            new_comment.save()
            form.save()
            return HttpResponse("article_detail")
    return render(request , "articles/detail.html",{"article":article , "form":form})
