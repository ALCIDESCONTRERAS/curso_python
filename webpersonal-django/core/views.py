from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html' )

def contact(request):
    return render(request, 'core/contact.html')
