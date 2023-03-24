from django.db import models


class Users(models.Model):
    Login = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    role = models.PositiveIntegerField(default=1)
    is_blocked = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)
    #phone = models.CharField(max_length=11, balnk=False, null=False)


class UserPhoto(models.Model):

    UserId = models.ForeignKey(Users, on_delete=models.DO_NOTHING, blank=False, null=False)

    exist = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='users_photos/')


class PostCategory(models.Model):
    category = models.CharField(max_length=255)

class Posts(models.Model):

    UserID = models.ForeignKey(Users, on_delete=models.DO_NOTHING, null=False, default=0)
    CategoryID = models.ForeignKey(PostCategory, on_delete=models.DO_NOTHING, null=False, default=0)

    Title = models.CharField(max_length=255)
    Text = models.CharField(max_length=255)
    Datee = models.DateTimeField(auto_now_add=True, null=True)



class Comments(models.Model):

    ParentCommentID = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    PostID = models.ForeignKey(Posts, on_delete=models.CASCADE)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)

    CommentText = models.CharField(max_length=255)
    Datee = models.DateTimeField(auto_now_add=True, null=True)

