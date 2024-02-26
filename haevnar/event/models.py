from django.db import models
from django.forms import ModelForm
from discordlogin.models import DiscordUser

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    emplacement = models.CharField(max_length=100)
    date = models.DateTimeField()
    created_by = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)