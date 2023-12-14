# Используем базовый образ Python
FROM python:3.8


# Устанавливаем зависимости
COPY ./requirements.txt /app/Main/requirements.txt
RUN pip install -r /app/Main/requirements.txt

# Копируем код приложения в контейнер
COPY . /app/Main

# Переходим в директорию приложения
WORKDIR /app/Main

# Указываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]