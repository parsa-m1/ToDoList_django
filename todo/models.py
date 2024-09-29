from django.db import models

from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title
