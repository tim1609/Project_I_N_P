from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group

admin.site.register(Post)
admin.site.register(Group)