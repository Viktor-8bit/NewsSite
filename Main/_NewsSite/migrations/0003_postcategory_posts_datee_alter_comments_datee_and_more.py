# Generated by Django 4.1.7 on 2023-03-24 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('_NewsSite', '0002_alter_comments_parentcommentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='Datee',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='Datee',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='UserID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='_NewsSite.users'),
        ),
        migrations.AlterField(
            model_name='userphoto',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='_NewsSite.users'),
        ),
        migrations.AddField(
            model_name='posts',
            name='CategoryID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='_NewsSite.postcategory'),
        ),
    ]
