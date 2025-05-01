from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='hello'),
    path('about/', views.about, name='about'),
	path('hello/<str:username>', views.hello, name='hello'),
    
]