from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
