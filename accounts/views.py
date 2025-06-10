from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm , CustomUserChangeForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.shortcuts import redirect
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def profile(request):
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})

def edit_profile(request):
    user = request.user
    form = CustomUserChangeForm(instance=user)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})