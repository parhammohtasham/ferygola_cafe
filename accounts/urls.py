from django.urls import path
from .views import SignUpView , profile , edit_profile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
