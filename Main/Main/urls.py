from django.contrib import admin
from django.urls import path
from _NewsSite import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include


urlpatterns = [

    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about'),
    path('create_post/', views.post_create_page, name='create_post'),
    path('post/', views.post, name='post'),
    path('post/category/', views.post_by_category, name='post_by_category'),
    path('post/get_comments', views.get_comments, name='get_comments'),
    path('post/delete_comment', views.delete_comment, name='delete_comment'),
    path('post/change_comment', views.change_comment, name='change_comment'),

    # я этого 100% не писал, видимо у нас завёлся хитрый хакер
    path('token/', obtain_auth_token),

    path('login/', views.my_login, name='login'),
    path('reg/', views.registration_page, name='reg'),
    path('logout/', views.my_logout, name='logout'),
    path('debug/', views.debug),
    path('admin/', admin.site.urls, name='admin'),
    
    # мне страшно удалять этот код
    # path('login/', views.LoginView.as_view(), name='login'),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),

    # path('test/', views.example_view),
]


