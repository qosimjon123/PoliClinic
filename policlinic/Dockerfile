# Используем последний образ Python
FROM python:latest

# Устанавливаем рабочую директорию
WORKDIR /var/project

# Копируем все файлы в контейнер
COPY . /var/project/


# Устанавливаем pipenv через pip
RUN pip install pipenv

# Явно указываем путь к Python при установке зависимостей
RUN pipenv install 


# Указываем команду для запуска сервера
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
