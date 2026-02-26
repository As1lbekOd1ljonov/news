from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.'
    )


class CategoryNews(models.Model):
    title = models.CharField(max_length=130)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news')
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    view = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True)
    updated_news = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(CategoryNews, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'news')


class SavedNews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='saved_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'news')

