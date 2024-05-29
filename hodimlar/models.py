import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
class Blog(models.Model):
    blog_name = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_name


class Department(models.Model):
    blog_name = models.ForeignKey(Blog, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    status = models.CharField(max_length=50, default='Active')
    phone = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images/', blank=True)
    blog = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    def get_username(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
