# Generated by Django 4.1.7 on 2023-04-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_NewsSite', '0009_alter_myusers_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
