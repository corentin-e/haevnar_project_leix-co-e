from django.db import models
from django.utils import timezone

from discordlogin.models import DiscordUser

# Create your models here.
class Actu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now, auto_now=False, verbose_name="Date de parution")
    image = models.ImageField(upload_to="actus/", null=True)
    created_by = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
