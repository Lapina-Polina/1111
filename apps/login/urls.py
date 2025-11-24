from django.urls import path
from .views import LoginView
from django.shortcuts import render

app_name = 'login'


def login_index(request):
    return render(request, 'login/index.html')


urlpatterns = [
    path('login-page/', login_index, name='login_index'),
    path('login/', LoginView.as_view(), name='login'),
]
