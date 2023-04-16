from django.contrib import admin

# Register your models here.
from .models import *
from rest_framework.authtoken.models import Token


class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'Login', 'email', 'password', 'role', 'is_blocked', 'date_create']
    list_display_links = ['id']
    search_fields = ['Login', 'email']
    list_editable = ['is_blocked', 'Login', 'password']
    list_filter = ['is_blocked']


admin.site.register(MyUsers, UsersAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'Title', 'Text', 'UserID', 'CategoryID', 'Datee']
    list_display_links = ['id']
    search_fields = ['Title', 'Text']

admin.site.register(Posts, PostAdmin)

admin.site.register(PostCategory)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'CommentText', 'PostID', 'UserID', 'Datee']
    list_display_links = ['id']
    list_editable = ['CommentText', 'UserID']
    search_fields = ['CommentText']
    list_filter = ['PostID', 'UserID']


admin.site.register(Comments, CommentsAdmin)

admin.site.register(UserPhoto)


# admin.site.register(Token)