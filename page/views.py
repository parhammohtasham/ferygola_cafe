from django.shortcuts import render
from .models import WeeklySchedule , Contact
from django.shortcuts import redirect
from .forms import ContactForm
import datetime
from django.utils.timezone import localtime
from django.db.models import Case, When, Value, IntegerField
from django.contrib import messages

def home(request):
    # گرفتن زمان لوکال با timezone درست (از تنظیمات Django)
    now = localtime()
    weekday_index = now.weekday()  # 0 = Monday, ..., 6 = Sunday

    # تطبیق با کلیدهای مدل WeeklySchedule
    day_order = ['pazartesi', 'salı', 'çarşamba', 'perşembe', 'cuma', 'cumartesi', 'pazar']
    today_slug = day_order[weekday_index]

    order = Case(*[When(day=day, then=Value(i)) for i, day in enumerate(day_order)], output_field=IntegerField())
    schedule = WeeklySchedule.objects.all().order_by(order)

    return render(request, 'pages/home.html', {
        'schedule': schedule,
        'today_slug': today_slug
    })

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    contact_list = Contact.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # به همین صفحه برمی‌گرده
    context = {'form': form, 'contact_list': contact_list}
    return render(request, 'pages/contact.html', context)