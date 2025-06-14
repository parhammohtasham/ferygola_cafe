from django.contrib import admin
from .models import Article , Comment
from django.contrib.admin import StackedInline
# Register your models here.

class CommentInLine(admin.StackedInline):
    model=Comment
    extra=1


class ArticleAdmin(admin.ModelAdmin):
    inlines=[CommentInLine]

admin.site.register(Article , ArticleAdmin)
admin.site.register(Comment)