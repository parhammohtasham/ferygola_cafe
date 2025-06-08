from django.contrib import admin
from . models import Category, Food
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    list_per_page = 10
    list_display_links = ("name",)
    list_max_show_all = 10

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "rate" , "is_active")
    list_filter = ("price", "rate" , "is_active")
    search_fields = ("name",)
    list_per_page = 10
    list_editable = ("rate",)
    list_display_links = ("name",)
    list_max_show_all = 10   