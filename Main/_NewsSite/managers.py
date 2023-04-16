from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
     Диспетчер пользовательских моделей пользователей,
     где электронная почта является уникальным идентификатором
     для аутентификации вместо имен пользователей.
    """
    def create_user(self, Login, password, email,  **extra_fields):
        """
          Создайте и сохраните пользователя с
          указанным адресом электронной почты и паролем.
        """
        Login = Login
        role = 'пользователь'
        is_staff = False
        is_superuser = False
        is_active = True
        email = self.normalize_email(email)
        MyUsers = self.model(email=email, **extra_fields)
        MyUsers.set_password(password)
        MyUsers.save()


        return MyUsers

    def create_superuser(self, password, email = 'main@.ru',  **extra_fields):

        role = 'администратор'
        is_staff = True
        is_superuser = True
        is_active = True
        email = self.normalize_email(email)
        MyUsers = self.model(email=email, **extra_fields)
        MyUsers.set_password(password)
        MyUsers.save()


        return MyUsers