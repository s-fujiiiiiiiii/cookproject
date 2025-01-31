from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model


class BlogPost(models.Model):
    user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    verbose_name='ユーザー',
    default=1
    )

    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )

    material = models.TextField(
        verbose_name='材料'
    )

    content = models.TextField(
        verbose_name='作り方'
    )

    tags = TaggableManager(
        verbose_name='タグ',
        blank=True
        )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    image1 = models.ImageField(
    verbose_name='写真',
    upload_to='photos',
    default='photos/default.jpg'
    )

    def __str__(self):
        return self.title