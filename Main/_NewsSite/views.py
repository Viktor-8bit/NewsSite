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
                    return render(request, 'reg.html', {'reg': RegForm(), 'error': 'пользователь с таким Login существует в базе !'})
                else:
                    user = Users()
                    user.email = regform.cleaned_data['email']
                    user.Login = regform.cleaned_data['Login']
                    user.password = hashlib.sha256(bytes(regform.cleaned_data['password'], 'utf-8')).hexdigest()
                    user.save()
            except:
                return render(request, 'reg.html', { 'reg': RegForm(), 'error': 'упс, где-то произошла ошибочка 😨'} )
        else:
            try:
                regform.clean()
            except Exception as ex:
                return render(request, 'reg.html', {'reg': RegForm(), 'error': ex.args[0]})

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
                    return HttpResponse(f'вы вошли')
                else:
                    return render(request, 'login.html', {'login': LoginFrom(), 'error': 'такого пользователя нет ️🐒️ или пароль неправильный 🐒️'})
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)

                return render(request, 'login.html', {'login': LoginFrom(), 'error': 'упс, где-то произошла ошибочка ☕'})
    return HttpResponse('неизвестная ошибка 🕷🕸')

def Post(request):
    posts = Posts.objects.order_by('-id')[:10]
    print(posts)
    return HttpResponse('hello page')

def index(request):
<<<<<<< Updated upstream
    # return HttpResponse('hello page')
    return render(request, 'main_page.html')
    # return render(request, 'test.html')
=======
    pass

def post_create_page(request):
    if request.method == 'POST':
        shadowlogin = ShadowLoginForm(request.POST)
        createpostfrom = PostForm(request.POST)

        if shadowlogin.is_valid():
            try:
                user = shadowlogin.check_access()
                if createpostfrom.is_valid():

                    _title = createpostfrom.cleaned_data['Title']
                    _text = createpostfrom.cleaned_data['Text']
                    _categoryId = createpostfrom.cleaned_data['CategoryID']

                    post = Posts()

                    post.UserID = user
                    post.Text = _text
                    post.Title = _title
                    post.CategoryID = _categoryId
                    #post.save()
                    return  HttpResponse('всё прошло гладко ✔')
                else:
                    return HttpResponse('не очень окей ❌')

            except Exception as ex:
                return HttpResponse(f'ошибка: не очень окей ❌ {ex.args[0]}')

        else:
            return HttpResponse('нет прав доступа')


        #print(createpostfrom.cleaned_data['Title'])
        #print(createpostfrom.cleaned_data['Text'])
        #print(createpostfrom.cleaned_data['CategoryID'])


            #createpostfrom.save()
            #return HttpResponse('всё окей ✔')
    if request.method == 'GET':
        return render(request, 'create_post.html', { 'create_post' : PostForm(), 'shadow_login' : ShadowLoginForm() })
>>>>>>> Stashed changes
