from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_view, name='categories'),
    path('<int:pk>/foods/', views.food_list, name='foods'),
]
