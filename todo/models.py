from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, timezone
from django.utils import timezone

# model manager
class TodoDoneManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_done=False)

class TodoRecentManager(models.Manager):

    def get_queryset(self):

        recent_todos_id = [todo.id for todo in Todo.objects.all() if todo.is_recent]
        return super().get_queryset().filter(id__in = recent_todos_id)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    objects = models.Manager()
    objects_done = TodoDoneManager()
    objects_recent = TodoRecentManager()

    class Meta:
        ordering = ['is_done', '-pub_date']

    def __str__(self):
        return self.title

    @property
    def is_recent(self):
        return True if self.pub_date + timedelta(days=1) > timezone.now() else False

