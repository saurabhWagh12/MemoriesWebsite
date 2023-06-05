from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MemoryCreator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    profileImage = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.user.username

class Memory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=400,blank=True)
    descrition = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    backgroundImage = models.ImageField(null=True,blank=True)
    favourite = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Images(models.Model):
    memory = models.ForeignKey(Memory,on_delete=models.CASCADE,null=True)
    image = models.ImageField(null=True,blank=True)
    nameImage = models.CharField(max_length=200,null=True,blank=True)


