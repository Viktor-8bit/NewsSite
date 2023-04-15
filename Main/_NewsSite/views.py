from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
import hashlib
import json

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
#страницы храняться по адресу NewsSite\Main\site_pages
# тестовый аккаунт - login: AMOGUS pass:  9E6-rH9-Ad9-FE6


from rest_framework.views import APIView
from rest_framework.response import Response


class Index(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



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
                    user = regform.save(commit=False)
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
                #print(password)
                User_count = Users.objects.filter(Login=login, password=password)

                if len(User_count) > 0:
                    return HttpResponse(f'вы вошли')
                else:
                    return render(request, 'login.html', {'login': LoginFrom(), 'error': 'такого пользователя нет ️🐒️ или пароль неправильный 🐒️'})
            except Exception as ex:
                #print(ex.args[0])
                return render(request, 'login.html', {'login': LoginFrom(), 'error': 'упс, где-то произошла ошибочка ☕'})
    return HttpResponse('неизвестная ошибка 🕷🕸')


def index(request): # 127.0.0.1:8000/

    log = True
    #log = False

    posts = Posts.objects.order_by('-id')[0:10] #posts = Posts.objects.filter(id__range =(0, 10))

    shadowlogin = ShadowLoginForm(request.POST)

    if shadowlogin.is_valid():
        try:
            user = shadowlogin.check_access()
        except Exception as ex:
            return render(request, 'main_page.html', {'posts': posts, 'log': log })

    return render(request, 'main_page.html', { 'posts' : posts, 'log' : log } )

def post_create_page(request): # 127.0.0.1:8000/create_post/
    if request.method == 'POST':
        shadowlogin = ShadowLoginForm(request.POST)
        createpostfrom = PostForm(request.POST)

        if shadowlogin.is_valid():
            try:
                user = shadowlogin.check_access()
                if createpostfrom.is_valid():

                    post = createpostfrom.save(commit=False)
                    post.UserID = user
                    post.save()

                    return  HttpResponse('всё прошло гладко ✔')
                else:
                    return HttpResponse('форма не прошла валидацию ❌')

            except Exception as ex:
                return HttpResponse(f'ошибка: не очень окей ❌ {ex.args[0]}')

        else:
            return HttpResponse('нет прав доступа, войдите в аккаунт или повысьте привелегии')

    if request.method == 'GET':
        return render(request, 'create_post.html', { 'create_post' : PostForm(), 'shadow_login' : ShadowLoginForm() })


def post(request): # 127.0.0.1:8000/post/

    if request.method == 'GET':
        try:
            id = int(request.GET['postid'])
            post = Posts.objects.get(id=id)
            return render(request, 'post_by_id.html', { 'post' : post, 'comentform': commentform, 'shadow_login' : ShadowLoginForm()})
        except Exception as ex:
            return HttpResponse(f'ошибка {ex.args[0]}')

    if request.method == 'POST': # добавить комментарий
        try:
            id = int(request.GET['postid'].replace('/', ''))
            post = Posts.objects.get(id=id)

            comform = commentform(request.POST)
            shadowlogin = ShadowLoginForm(request.POST)

            if shadowlogin.is_valid():
                try:
                    user = shadowlogin.check_access()
                    if comform.is_valid():

                        comment = comform.save(commit=False)

                        comment.PostID = post;

                        comment.UserID = user;
                        comment.save();

                        return render(request, 'post_by_id.html', {'post': post, 'comentform': commentform, 'shadow_login': ShadowLoginForm()})
                    else:
                        return HttpResponse('форма не прошла валидацию ❌')

                except Exception as ex:
                    return HttpResponse(f'ошибка: не очень окей ❌ {ex.args[0]}')

            else:
                return HttpResponse('нет прав доступа, войдите в аккаунт или повысьте привелегии')


            return render(request, 'post_by_id.html', {'post': post, 'comentform': commentform})
        except Exception as ex:
            return render(request, 'post_by_id.html', {'post': post, 'comentform': commentform, 'error': ex.args[0]})


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
            coments = Comments.objects.filter(PostID = post_id).order_by('-Datee')
            to_return = { 'comments' : [] }
            for com in coments:
                if com.ParentCommentID is None:
                    to_return['comments'].append( { 'id': str(com.id) ,'text' : str(com.CommentText), 'dat' : str(com.Datee)[0:19], 'name' : com.UserID.Login, 'parent' : com.ParentCommentID } )
                else:
                    pass

            return HttpResponse( json.dumps(to_return, ensure_ascii=False)); # json.dumps( {'sus' : ['dfdf', 'fdfdf', 'dfdds'] } | json.dumps(coments.__dict__)
        except Exception as ex:
            return HttpResponse(f"ошибка получения комментариев {ex.args[0]}")

def logout(request):
    return render(request, 'logout.html')