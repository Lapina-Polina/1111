from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request):
        # Показываем форму логина
        return render(request, 'login/index.html')

    def post(self, request):
        # Получаем данные из POST-запроса
        email = request.POST.get('email')
        password = request.POST.get('password')
        return JsonResponse({
            'email': email,
            'password': password
        })
