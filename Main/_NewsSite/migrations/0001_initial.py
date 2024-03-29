# Generated by Django 4.1.7 on 2023-03-18 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('role', models.PositiveIntegerField(default=1)),
                ('is_blocked', models.BooleanField(default=False)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exist', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to='users_photos/')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_NewsSite.users')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Text', models.CharField(max_length=255)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='_NewsSite.users')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CommentText', models.CharField(max_length=255)),
                ('Datee', models.DateTimeField(auto_now_add=True)),
                ('ParentCommentID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='_NewsSite.comments')),
                ('PostID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_NewsSite.posts')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_NewsSite.users')),
            ],
        ),
    ]
