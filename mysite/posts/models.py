from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField("group name", max_length=200)
    slug = models.SlugField(unique=True, verbose_name='URL', max_length=20)
    describtion = models.TextField("Describtion"
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    poem = models.TextField()
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='groups',
        blank=True,
        null=True
        )
    image = models.ImageField( 'Картинка',upload_to='posts/', blank=True)
