from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name