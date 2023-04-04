from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
import hashlib
import json

#страницы храняться по адресу NewsSite\Main\site_pages
# тестовый аккаунт - login: AMOGUS pass:  9E6-rH9-Ad9-FE6

def registration_page(request): # 127.0.0.1:8000/reg/
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

def login_page(request): # 127.0.0.1:8000/log/
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


def index(request): # 127.0.0.1:8000/
    # count = (Posts.objects.count())
    posts = Posts.objects.order_by('-id')[0:9]
    #posts = Posts.objects.filter(id__range =(0, 10))
    return render(request, 'main_page.html', { 'posts' : posts } )

def post_create_page(request): # 127.0.0.1:8000/create_post/
    if request.method == 'POST':
        shadowlogin = ShadowLoginForm(request.POST)
        createpostfrom = PostForm(request.POST)

        if shadowlogin.is_valid():
            try:
                user = shadowlogin.check_access()
                if createpostfrom.is_valid():

                    post = Posts()

                    post.UserID = user
                    post.Text = createpostfrom.cleaned_data['Text']
                    post.Title = createpostfrom.cleaned_data['Title']
                    post.CategoryID = createpostfrom.cleaned_data['CategoryID']
                    post.save()
                    return  HttpResponse('всё прошло гладко ✔')
                else:
                    return HttpResponse('не очень окей ❌')

            except Exception as ex:
                return HttpResponse(f'ошибка: не очень окей ❌ {ex.args[0]}')

        else:
            return HttpResponse('нет прав доступа')

    if request.method == 'GET':
        return render(request, 'create_post.html', { 'create_post' : PostForm(), 'shadow_login' : ShadowLoginForm() })


def post(request): # 127.0.0.1:8000/post/
    if request.method == 'GET':
        try:
            id = int(request.GET['postid'])
            post = Posts.objects.get(id=id)
            return render(request, 'post_by_id.html', { 'post' : post })
        except Exception as ex:
            return HttpResponse(f'ошибка {ex.args[0]}')

def post_by_category(request): # 127.0.0.1:8000/post/category/
    try:
        id = int(request.GET['cid']) # в базе есть 9 и 3
        posts = Posts.objects.filter(CategoryID=PostCategory.objects.get(id=id))
        return render(request, 'get_post_by_category.html', {'posts' : posts})

    except Exception as ex:
        print(ex.args[0])
        return HttpResponse(ex.args[0])

def get_comments(request): # 127.0.0.1:8000/post/get_comments
    if request.method == 'GET':
        try:
            post_id = int(request.GET['cid'])
            coments = Comments.objects.filter(PostID = post_id)

            to_return = { 'comments' : [] }

            for com in coments:
                if com.ParentCommentID is None:
                    to_return['comments'].append( { 'text' : str(com.CommentText), 'dat' : str(com.Datee), 'name' : com.UserID.Login, 'parent' : com.ParentCommentID } )
                else:
                    pass
            print(to_return['comments'])


            return HttpResponse( json.dumps(to_return, ensure_ascii=False)); # json.dumps( {'sus' : ['dfdf', 'fdfdf', 'dfdds'] } | json.dumps(coments.__dict__)
        except Exception as ex:
            print(f"ошибка получения комментариев {ex.args[0]}")
            return HttpResponse(f"ошибка получения комментариев {ex.args[0]}")
