from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import posts

admin.site.register(posts)
