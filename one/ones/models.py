from django.db import models
class Ball(models.Model):
    Ball = models.CharField(max_length=100)
    Color = models.CharField(max_length=100)
    About = models.TextField()
    def __str__(self):
        return (self.name)
# Create your models here.
