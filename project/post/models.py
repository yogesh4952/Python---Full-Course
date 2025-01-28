from django.db import models

# Create your models here
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FormData(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    is_checked = models.BooleanField(default=False)  # For the checkbox

    def __str__(self):
        return f"{self.name} - {self.email}"