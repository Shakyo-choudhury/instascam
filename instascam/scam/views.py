# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def register_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'clickbait.html')
    else:
        form = ContactForm()
    
    return render(request, 'clickbait.html', {'form': form})

def home(request):
    return render(request, "login.html")

def bait(request):
    return render(request, 'clickbait.html')
