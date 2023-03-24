from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
import hashlib

#страницы храняться по адресу NewsSite\Main\site_pages
# тестовый аккаунт - login: AMOGUS pass:  9E6-rH9-Ad9-FE6

def registration_page(request):
    if request.method == 'GET':
        return render(request, 'reg.html', { 'reg': RegForm() })
    elif request.method == 'POST':
        regform = RegForm(request.POST)
        if regform.is_valid():
            try:
                User_count = Users.objects.filter(Login =regform.cleaned_data['Login']).count()
                if User_count > 0:
                    return render(request, 'reg.html', {'reg': RegForm(), 'error': 'пользователь с таким Login существует в базе, не взламывайте его перебором паролей пожалуйста 😏!!!'})
                else:
                    user = Users()
                    user.email = regform.cleaned_data['email']
                    user.Login = regform.cleaned_data['Login']
                    user.password = hashlib.sha256(bytes(regform.cleaned_data['password'], 'utf-8')).hexdigest()
                    user.save()
            except:
                return render(request, 'reg.html', { 'reg': RegForm(), 'error': 'упс, где-то произошла ошибочка 😨'} )
        return HttpResponse('Вы скорее всего успешно зарегистрированы 😎')

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'login': LoginFrom()})
    elif request.method == 'POST':
        loginform = LoginFrom(request.POST)
        if loginform.is_valid():
            try:
                login = loginform.cleaned_data['Login']
                password = hashlib.sha256(bytes(loginform.cleaned_data['password'], 'utf-8')).hexdigest()
                print(password)
                User_count = Users.objects.filter(Login=login, password=password)

                if len(User_count) > 0:
                    print(User_count[0])
                    return HttpResponse(f'аккаунт существует 🍵 с логином {login} и паролем {password} 🍵')
                else:
                    return render(request, 'login.html', {'login': LoginFrom(), 'error': 'такого пользователя нет ️🐒️ или пароль неправильный 🐒️'})
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)

                return render(request, 'login.html', {'login': LoginFrom(), 'error': 'упс, где-то произошла ошибочка ☕'})
    return HttpResponse('неизвестная ошибка 🕷🕸')

def index(request):
    # return HttpResponse('hello page')
    return render(request, 'main_page.html')
    # return render(request, 'test.html')