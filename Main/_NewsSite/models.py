from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class MyUsers(AbstractBaseUser, PermissionsMixin):
    role = models.CharField(max_length=255, blank=True, null=True)
    Login = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, blank=True, null=True)
#    password = models.CharField(max_length=255, blank=False, null=False)
#    role = models.PositiveIntegerField(default=1)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'Login'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_blocked = models.BooleanField(default=False)

    date_create = models.DateTimeField(auto_now_add=True)
    #phone = models.CharField(max_length=11, null=True)
    class Meta:
        verbose_name = 'Пользователи'
        ordering = [ 'date_create' ]
    def __str__(self):
        return 'Пользователь: {}'.format(self.Login)

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()

class UserPhoto(models.Model):

    UserId = models.ForeignKey(MyUsers, on_delete=models.DO_NOTHING, blank=False, null=False)
    exist = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='users_photos/')

    class Meta:
        verbose_name = 'Аватарки'
    def __str__(self):
        return 'Фото: {}'.format(self.UserId)

class PostCategory(models.Model):
    category = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Категории'
        ordering = [ 'category' ]
    def __str__(self):
        return 'Категория: {}'.format(self.category)

class Posts(models.Model):

    UserID = models.ForeignKey(MyUsers, on_delete=models.DO_NOTHING, null=False, default=0)
    CategoryID = models.ForeignKey(PostCategory, on_delete=models.DO_NOTHING, null=False, default=0)

    Title = models.CharField(max_length=255)
    Text = models.CharField(max_length = 10000 )
    Datee = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        verbose_name = 'Посты'
        ordering = [ 'Datee' ]

    def __str__(self):
        return 'Пост: {}'.format(self.Title)


class Comments(models.Model):

    ParentCommentID = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default = None)
    PostID = models.ForeignKey(Posts, on_delete=models.CASCADE)
    UserID = models.ForeignKey(MyUsers, on_delete=models.CASCADE)

    CommentText = models.CharField(max_length=255)
    Datee = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Коментарии'
        ordering = [ 'Datee' ]
    def __str__(self):
        return 'Коментарий: {}'.format(self.CommentText)