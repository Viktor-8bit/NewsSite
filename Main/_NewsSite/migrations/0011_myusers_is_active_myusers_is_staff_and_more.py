# Generated by Django 4.1.7 on 2023-04-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_NewsSite', '0010_alter_myusers_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusers',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myusers',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myusers',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
