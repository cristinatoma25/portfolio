from django.db import models
import time

class User(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    quetions = models.TextField(max_length=300)

    def __str__(self):
        return self.name