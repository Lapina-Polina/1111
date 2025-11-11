from django.urls import path
from django.shortcuts import render
from .views import LoginView

def login_index(request):
    return render(request, 'login/index.html')

urlpatterns = [
    path('', login_index, name='login_index'),
    path('', LoginView.as_view(), name='login_index'),
]