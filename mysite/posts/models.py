
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField("PostsText")
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Author'
                               )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Author",
        blank=True,
        null=True)

    def __str__(self):
        return self.text


class Group(models.Model):
      title = models.CharField("group name", max_length=200)
      slug = model.Slug.Field(unique=True, verbose_name="URL", max_length=20)
      description = models.TextField("Description")

      def __str__(self):
          return self.title
