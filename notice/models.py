from django.db import models
from django.contrib.auth.models import User
from category.models import Category


# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notices')
    description = models.TextField(blank=True, null=True)
    preview = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='notices/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.user.username} em {self.post.title}'