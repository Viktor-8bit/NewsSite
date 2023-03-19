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

    UserId = models.ForeignKey(Users, blank=False, null=False, on_delete=models.CASCADE)

    exist = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='users_photos/')


class Posts(models.Model):

    UserID = models.ForeignKey(Users, on_delete=models.DO_NOTHING, null=False, blank=False)

    Title = models.CharField(max_length=255)
    Text = models.CharField(max_length=255)


class Comments(models.Model):

    ParentCommentID = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    PostID = models.ForeignKey(Posts, on_delete=models.CASCADE)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)

    CommentText = models.CharField(max_length=255)
    Datee = models.DateTimeField(auto_now_add=True)