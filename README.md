
# Социальная сеть Post.It
![apple-touch-icon](https://user-images.githubusercontent.com/91019022/170825099-ddd3a186-b470-46f3-b8ad-cab3eaa008ce.png)




Пользователи могут выкладывать в свой профиль посты, указывать категории и тэги к ним. 
Другие юзеры тем временем могут реагировать на пост, комментировать его, а также подписываться друг на друга.
## Для запуска

### Установка зависимостей

> pip install -r requirements.txt 

### Создание виртуального окружения

> echo > .env 'SECRET_KEY="your-secret-key"\nDEBUG=True' 

### Создание и обновление базы данных

> python manage.py migrate

### Запуск сервера

> python manage.py runserver
