from django.contrib import admin

from .models import Category, News, Comment

# Добавление модели на главную страницу интерфейса администратора
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Comment)


