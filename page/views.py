from django.shortcuts import render
from .models import WeeklySchedule , Contact
from django.shortcuts import redirect
from .forms import ContactForm
# Create your views here.

def home(request):
    schedule = WeeklySchedule.objects.all()
    return render(request, 'pages/home.html', {'schedule': schedule})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    contact_list = Contact.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success pages
    context = {'form': form , 'contact_list': contact_list}
    return render(request, 'pages/contact.html', context)
