from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('quoteoutput/', views.quoteout, name='polls-quoteout'),
    path('quoteinput/', views.quotein, name='polls-quotein'),    
]