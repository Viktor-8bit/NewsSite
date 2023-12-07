from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
import hashlib
import json

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import serializers


from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from rest_framework import status
from .managers import *



#страницы храняться по адресу NewsSite\Main\site_pages
# тестовe аккаунты

# админ
# login: sus | pass: 123

# пользователь
# login: user | pass: 123

def my_login(request):

    if request.method == 'GET':

        error = ''
        try:
            if request.GET['error'] != '':
                error = request.GET['error']
        except Exception as ex:
            pass
        print(error)
        return render(request, 'login.html', {'login': LoginFrom(), 'error': error})

def my_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect(f'/{request.GET["redir"].replace("/", "") }')
    else:
        pass # (╯°□°）╯︵ ┻━┻ ЭТА ФУНКЦИЯ РАБОТАЕТ ТОЛЬКО С GET !!!

def registration_page(request): # 127.0.0.1:8000/reg/
    if request.method == 'GET':
        return render(request, 'reg.html', { 'reg': RegForm() })
    elif request.method == 'POST':
        regform = RegForm(request.POST)
        if regform.is_valid():
            try:
                User_count = MyUsers.objects.filter(Login =regform.cleaned_data['Login']).count()
                if User_count > 0:
                    return render(request, 'reg.html', {'reg': RegForm(), 'error': 'пользователь с таким Login существует в базе !'})
                else:
                    user = regform.save(commit=False)
                    user.set_password(regform.cleaned_data['password'])
                    # user.save()
            except:
                pass
        else:
            try:
                regform.clean()
            except Exception as ex:
                return render(request, 'reg.html', {'reg': RegForm(), 'error': ex.args[0]})
        return redirect('/')

def index(request): # 127.0.0.1:8000/ главная страница
    posts = Posts.objects.order_by('-id')[0:12]  # posts = Posts.objects.filter(id__range =(0, 10))
    # для форм или js
    if request.method == 'POST':

        loginform = LoginFrom(request.POST)
        if loginform.is_valid():
            user = authenticate(Login=loginform.cleaned_data['Login'], password=loginform.cleaned_data['password'])
            print(user)
            if (user is not None):
                login(request, user)
                return render(request, 'main_page.html', {'posts': posts})
            else:
                return redirect('login/?&error=пользователь не найден или неверный пароль')
        else:
            pass  # что-то пошло не так упс ╰(*°▽°*)╯
    else:
        return render(request, 'main_page.html', { 'posts' : posts } )

def post_create_page(request): # 127.0.0.1:8000/create_post/
    if request.method == 'POST':
        createpostfrom = PostForm(request.POST)

        try:
            if createpostfrom.is_valid():

                if not request.user.is_authenticated:
                    return render(request, 'create_post.html', {'create_post': PostForm(), 'error': 'вы не вошли в аккаунт'})

                elif request.user.is_superuser != True:
                    return render(request, 'create_post.html', {'create_post': PostForm(), 'error': 'у вас не прав для этой операции (╯°□°）╯︵ ┻━┻'})

                else:
                    user = request.user
                    post = createpostfrom.save(commit=False)
                    post.UserID = user
                    post.save()

                    return  redirect('/')
            else:
                return HttpResponse('форма не прошла валидацию (╯°□°）╯︵ ┻━┻')

        except Exception as ex:
            return HttpResponse(f'ошибка: не очень окей ❌ {ex.args[0]}')


    if request.method == 'GET':
        return render(request, 'create_post.html', { 'create_post' : PostForm() })

def post(request): # 127.0.0.1:8000/post/

    if request.method == 'GET':
        try:
            id = int(request.GET['postid'])
            post = Posts.objects.get(id=id)
            return render(request, 'post_by_id.html', { 'post' : post, 'comentform': commentform })
        except Exception as ex:
            print(f'ошибка {ex.args[0]}')


    if request.method == 'POST': # добавить комментарий
        try:
            id = int(request.GET['postid'].replace('/', ''))
            post = Posts.objects.get(id=id)

            comform = commentform(request.POST)

            if comform.is_valid():
                if not request.user.is_authenticated:
                    return render(request, 'post_by_id.html', {'post': post, 'comentform': commentform, 'error': 'вы не вошли в аакаунт ⚠'})

                else:
                    user = request.user
                    comment = comform.save(commit=False)

                    comment.PostID = post;

                    comment.UserID = user;
                    comment.save();

                    return render(request, 'post_by_id.html', {'post': post, 'comentform': commentform })
            else:
                return HttpResponse('форма не прошла валидацию (╯°□°）╯︵ ┻━┻')

        except Exception as ex:
            return render(request, 'post_by_id.html', {'post': post, 'comentform': commentform, 'error': ex.args[0]})

def post_by_category(request): # 127.0.0.1:8000/post/category/
    try:
        id = int(request.GET['cid']) # в базе есть 9 и 3
        posts = Posts.objects.filter(CategoryID=PostCategory.objects.get(id=id))
        return render(request, 'get_post_by_category.html', {'posts' : posts, 'post_category' : posts[0].CategoryID.category, 'categorys' : PostCategory.objects.all() })

    except Exception as ex:
        print(ex.args[0])
        return HttpResponse(ex.args[0])

def debug(request):
    return render(request, 'amogus.html')

def delete_comment(request):

    if request.method == 'GET':
        print(request.user)
        if not request.user.is_authenticated:
            pass # ВОЙДИТЕ СНАЧАЛА В АККАУНТ (╯°□°）╯︵ ┻━┻
        else:
            try:
                Login = request.user.Login
                id = int(request.GET['id'])
                post_id = int(request.GET['pid'])

                if id != None:
                    comment = Comments.objects.get(id = id)
                    print(comment, id)
                    if comment.UserID.Login == Login:
                        print(comment)
                        comment.delete()
                        coments = Comments.objects.filter(PostID=post_id).order_by('-Datee')
                        to_return = {'comments': []}
                        for com in coments:
                            if com.ParentCommentID is None:
                                to_return['comments'].append(
                                    {'id': str(com.id), 'text': str(com.CommentText), 'dat': str(com.Datee)[0:19], 'name': com.UserID.Login, 'parent': com.ParentCommentID})
                            else:
                                pass

                        return HttpResponse(json.dumps(to_return, ensure_ascii=False));  # json.dumps( {'sus' : ['dfdf', 'fdfdf', 'dfdds'] } | json.dumps(coments.__dict__) успех (¬‿¬)
                    else:
                        pass # НЕЛЬЗЯ УДАЛЯТЬ ЧУЖИЕ КОММЕНТАРИИ БЕЗ ПРАВ АДМИНИСТРАТОРА (╯°□°）╯︵ ┻━┻

            except Exception as ex:
                return HttpResponse(f'опять ошибка: {ex.args[0]} (╯°□°）╯︵ ┻━┻')
    else:
        return HttpResponse('РАБОТАТЬ С delete_comment МОЖНО ТОЛЬКО ЧЕРЕЗ POST (╯°□°）╯︵ ┻━┻')

def change_comment(request):

    if request.method == 'GET':
        print(request.user)
        if not request.user.is_authenticated:
            return HttpResponse('ВОЙДИТЕ СНАЧАЛА В АККАУНТ (╯°□°）╯︵ ┻━┻')
        else:
            try:
                Login = request.user.Login
                id = int(request.GET['id'])
                post_id = int(request.GET['pid'])
                text = request.GET['text']

                if id != None:
                    comment = Comments.objects.get(id = id)
                    print(comment, id)
                    if comment.UserID.Login == Login:
                        comment.CommentText = text
                        comment.save()
                        print(comment)
                        coments = Comments.objects.filter(PostID=post_id).order_by('-Datee')
                        to_return = {'comments': []}
                        for com in coments:
                            if com.ParentCommentID is None:
                                to_return['comments'].append(
                                    {'id': str(com.id), 'text': str(com.CommentText), 'dat': str(com.Datee)[0:19], 'name': com.UserID.Login, 'parent': com.ParentCommentID})
                            else:
                                pass

                        return HttpResponse(json.dumps(to_return, ensure_ascii=False));  # json.dumps( {'sus' : ['dfdf', 'fdfdf', 'dfdds'] } | json.dumps(coments.__dict__)
                        #return HttpResponse('успех (¬‿¬)')
                    else:
                        return HttpResponse('НЕЛЬЗЯ УДАЛЯТЬ ЧУЖИЕ КОММЕНТАРИИ БЕЗ ПРАВ АДМИНИСТРАТОРА (╯°□°）╯︵ ┻━┻')

            except Exception as ex:
                return HttpResponse(f'опять ошибка: {ex.args[0]} (╯°□°）╯︵ ┻━┻')
    else:
        return HttpResponse('РАБОТАТЬ С delete_comment МОЖНО ТОЛЬКО ЧЕРЕЗ POST (╯°□°）╯︵ ┻━┻')

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
            pass # ошибка получения комментариев

def about_us(request):
    return render(request, 'about.html')