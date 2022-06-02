from django.contrib.auth import get_user_model
from django.db import models


class Motorcycle(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    make = models.CharField(max_length=64)
    year = models.CharField(max_length=20)
    model = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.make