from django.contrib import admin
from django.urls import path
from _NewsSite import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include


urlpatterns = [

    path('', views.index),
    path('about_us/', views.about_us),
    path('create_post/', views.post_create_page),
    path('post/', views.post),
    path('post/category/', views.post_by_category),
    path('post/get_comments', views.get_comments),
    path('post/delete_comment', views.delete_comment),
    path('post/change_comment', views.change_comment),

    path('token/', obtain_auth_token),
    path('login/', views.my_login),
    path('reg/', views.registration_page),
    path('logout/', views.my_logout),
    path('debug/', views.debug),
    path('admin/', admin.site.urls),
#    path('login/', views.LoginView.as_view(), name='login'),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),

    # path('test/', views.example_view),
]

