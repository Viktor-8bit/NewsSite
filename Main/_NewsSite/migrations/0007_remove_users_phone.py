# Generated by Django 4.1.7 on 2023-04-14 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_NewsSite', '0006_alter_comments_options_alter_postcategory_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='phone',
        ),
    ]
