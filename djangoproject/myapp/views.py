from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Index Page')

def hello(request, username):
    return HttpResponse('<h1>Hello World! %s</h1>' % username)

def about(request):
    return HttpResponse('<h1>About</h1>')