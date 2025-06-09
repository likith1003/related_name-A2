from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50, unique=True)
    add = models.TextField()
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=150)
    desc = models.TextField()

    def __str__(self):
        return f"{self.user.username}({self.title[:10]})"